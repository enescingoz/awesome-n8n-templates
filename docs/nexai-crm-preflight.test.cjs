// Behavioral checks for the original preflight resource, using fictional records.
const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const path = require('node:path');
const p = path.join(__dirname, "..", "Other_Integrations_and_Use_Cases/Preflight a CRM import and route conflicting duplicates for human review.json");
const w = JSON.parse(fs.readFileSync(p, 'utf8'));
const code = w.nodes.find(n => n.name === 'Validate and classify batch').parameters.jsCode;
const execute = (batch, extraItems=[]) => JSON.parse(JSON.stringify(vm.runInNewContext('(function(){'+code+'})()', {$input:{all:()=>[{json:batch},...extraItems]}})[0].json));
const row = (sourceId,email,company='Example')=>({sourceId,email,company});
const batch = records=>({batchId:'test',records,existingContacts:[]});
let count=0;
const check=(name,fn)=>{fn();count++;console.log('PASS '+name);};
check('Conflicts hold every row, regardless of input order',()=>{
  for(const records of [[row('a','x@example.invalid','A'),row('b','x@example.invalid','B')],[row('b','x@example.invalid','B'),row('a','x@example.invalid','A')]]){
    const d=execute(batch(records));assert.equal(d.summary.human_review,2);assert.equal(d.summary.ready_for_mapping,0);
  }
});
check('Identical duplicates leave exactly one mapping candidate',()=>{
  const d=execute(batch([row('a',' X@example.invalid '),row('b','x@example.invalid')]));assert.equal(d.summary.ready_for_mapping,1);assert.equal(d.summary.skip_identical_batch_duplicate,1);
});
check('A reused source ID holds both different email records',()=>{
  const d=execute(batch([row('a','x@example.invalid'),row('a','y@example.invalid')]));assert.equal(d.summary.human_review,2);
});
check('An invalid member holds the entire matching duplicate group',()=>{
  const d=execute(batch([row('','x@example.invalid'),row('b','x@example.invalid')]));assert.equal(d.summary.human_review,2);
});
check('Two CRM IDs are ambiguous, repeated same CRM ID is not',()=>{
  const b=batch([row('a','x@example.invalid')]);b.existingContacts=[{email:'x@example.invalid',crmId:'1'},{email:'x@example.invalid',crmId:'2'}];assert.equal(execute(b).summary.human_review,1);
  b.existingContacts[1].crmId='1';const d=execute(b);assert.equal(d.decisions[0].proposedAction,'map_existing');assert.equal(d.decisions[0].crmId,'1');
});
check('An empty batch produces explicit zero counts',()=>assert.equal(execute(batch([])).summary.total,0));
check('Malformed batches and snapshots fail loudly',()=>{
  for(const b of [{}, {...batch([]),records:[null]}, {...batch([]),existingContacts:[{email:'invalid',crmId:'1'}]}, {...batch([]),batchId:''}])assert.throws(()=>execute(b));
  assert.throws(()=>execute(batch([]),[{json:batch([])}]));
});

console.log(JSON.stringify({behavioral_checks_passed:count,fictional_data_only:true}));

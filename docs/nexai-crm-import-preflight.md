# CRM contact import preflight for n8n

Check one contact-import batch before connecting a write step to a CRM. This workflow separates records ready for field mapping, conflicts that need a person, and identical duplicates within the supplied batch. It includes a fictional sample and makes no external requests or CRM writes.

Author: [NexAi](https://nex-ai.co/en/). This original workflow was developed with AI assistance. All examples are fictional.

## What the example does

The input contains a batch ID, a contact snapshot and ten fictional import rows. The classifier trims and lowercases email keys, checks the required fields, compares duplicate groups and looks for ambiguous matches in the supplied snapshot.

The expected sample report is:

| Decision | Rows | Meaning |
| --- | --- | --- |
| Ready for field mapping | 2 | One candidate for a new record and one for an existing record; neither is written anywhere. |
| Human review | 7 | Conflicting duplicates, reused source identifiers, missing fields, invalid email shape or ambiguous CRM matches. |
| Skip identical batch duplicate | 1 | A later row with the same normalized email and company as an earlier valid row. |

The workflow has a summary output, a mapping-candidate output and a combined review/skipped output. The combined output contains eight rows in the sample: seven held for review and one marked for skipping.

## Try it

1. Import the workflow JSON into a separate n8n test workspace.
2. Leave the fictional input in place and run the manual trigger.
3. Inspect `Read batch summary`, `Rows ready for field mapping`, and `Human review and skipped duplicates`.
4. Change one fictional row at a time to explore the classification rules.

No credentials are required. Replace the fictional input only with information you are authorized to use. Check the rules with the process owner before adapting this example for a real import.

## Boundaries

- An email-shape check does not verify mailbox existence or permission to contact someone. Lowercasing an email key is an explicit policy in this example; confirm your matching policy before reusing it.
- Only email and company are compared. If other mapped fields matter, add them to the conflict rules.
- An empty snapshot means no existing contacts were supplied. It does not show that a CRM is empty.
- A repeated run reproduces a preflight report. This example has no persistent idempotency ledger and does not protect a later CRM write by itself.
- A mapping candidate is not an approved production change. Decide field ownership, exception handling and human approval before connecting write operations.

## Validation

Validated with n8n 2.45.7 and Node.js 24.22.2 on 1 November 2026. Two fresh, isolated SQLite instances executed all six processing nodes successfully across an export/import roundtrip. The sample produced the expected 2 mapping candidates, 7 human-review decisions and 1 skipped duplicate. The classifier source was unchanged by the roundtrip.

The seven behavioral checks can be run from the repository root with `node docs/nexai-crm-preflight.test.cjs`. The exact publication artifact also passed import, execution and an export/import roundtrip in two further fresh databases.

The local behavioral tests cover conflicting duplicates in both input orders, identical duplicates, reused source IDs, invalid members of duplicate groups, ambiguous snapshots, empty batches and malformed input. Every example is synthetic.

## License

This contribution follows the collection’s Creative Commons Attribution 4.0 license. Give credit to NexAi when reusing this original workflow; see the repository license. No endorsement by n8n or the collection’s maintainer is claimed.

# Report — HR Offer Letter Generator

## Business Use Case
HR managers spend significant time drafting offer letters for new hires. 
Since offer letters follow a predictable structure but require per-hire 
customization, this is a strong candidate for LLM-assisted drafting. 
The target user is a hiring manager who provides candidate details and 
receives a draft letter ready for human review before sending.

## Model Choice
I used GPT-3.5-turbo via the OpenAI API. It is low-cost, fast, and 
sufficient for structured business writing tasks like this one. No other 
models were tested, but a more capable model like GPT-4 would likely 
produce fewer placeholder artifacts in the output.

## Baseline vs. Final Design

**Version 1 (Baseline):** The initial prompt produced a structured letter 
but included many bracket placeholders throughout the body such as 
[Company Name], [Your Name], and [Phone Number].

**Version 2 (Revision 1):** Added instructions to omit placeholder fields 
entirely. Removed most body placeholders but the model still awkwardly 
mentioned stock options not being part of the offer.

**Version 3 (Revision 2):** Tightened omission instructions. Output became 
clean and professional with placeholders limited to the signature block, 
which is appropriate for human completion.

## Eval Set Results

| Case | Result |
|------|--------|
| Case 1 — Normal (Marketing Coordinator) | Clean, accurate output |
| Case 2 — Normal (Account Executive) | Best output, no invented commission structure |
| Case 3 — Edge Case (Contract) | Failed: wrote $55/year instead of $55/hour |
| Case 4 — Edge Case (Relocation) | Failed: ignored relocation assistance, invented benefits package |
| Case 5 — Equity Compensation | Better than expected: did not invent vesting terms |

## Where the Prototype Still Fails

The prototype has three notable failure areas. First, it mishandles hourly 
rate inputs, defaulting to annual salary framing. Second, it does not 
reliably incorporate additional fields like relocation assistance. Third, 
minor placeholders like [Date] and [specific date] persist across outputs. 
All outputs require human review before sending.

## Deployment Recommendation
I would not recommend deploying this prototype without tighter review 
controls. It performs well on standard full-time hires but fails on edge 
cases involving contract roles and additional compensation fields. A 
reasonable deployment would use this as a first-draft tool where a human 
HR manager reviews and edits every output before it is sent to a candidate.

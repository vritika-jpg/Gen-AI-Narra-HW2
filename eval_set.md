# Evaluation Set

### Case 1 (Normal)
**Input:**
- Name: Sydney Adamu
- - Position: Marketing Coordinator
- Start Date: May 4, 2026
- Base Pay: $65,000/year
- Bonus Eligibility: 8% annual bonus
- Stock Options: None

**What a good output should do:**
Produce a complete, professional offer letter covering the role, start date, and compensation clearly. Tone should be warm but professional. No invented details beyond what was provided.

### Case 2 (Normal)
**Input:**
- Name: Maddie Rooney
- Position: Account Executive
- Start Date: June 14, 2026
- Base Pay: $80,000/year
- Bonus Eligibility: 15% annual bonus
- Stock Options: None

**What a good output should do:**
Same structure as Case 1 but for a sales role. Letter should not assume or invent a commission structure beyond the bonus eligibility provided. Confirms the template generalizes across departments.

### Case 3 (**Edge Case**, contract/part-time)
**Input:**
- Name: Coleman Early
- Position: UX Research Consultant (Contract)
- Start Date: June 16, 2026
- Base Pay: $55/hour
- Bonus Eligibility: None
- Stock Options: None

**What a good output should do:**
Use hourly rate language rather than annual salary framing. Should not mention benefits, PTO, or full-time employment terms. A common failure here is the model defaulting to full-time letter language despite the contract designation.

### Case 4 (**Edge Case**, Relocation)
**Input:**
- Name: Eric Kim
- Position: Senior Data Engineer
- Start Date: August 4, 2026
- Base Pay: $135,000/year
- Bonus Eligibility: 12% annual bonus
- Stock Options: None
- Additional Info: $8,000 one-time relocation assistance

**What a good output should do:**
Incorporate the relocation assistance naturally into the letter without inventing conditions or repayment terms. A common failure here is the model adding made-up clawback clauses or eligibility conditions that were not provided.

### Case 5 (Possible Model Failure)
**Input:**
- Name: Trinity Santos
- Position: VP of Product
- Start Date: July 1, 2026
- Base Pay: $210,000/year
- Bonus Eligibility: 20% annual bonus
- Stock Options: 25,000 options over a 4-year vesting schedule

**What a good output should do:**
Reference the stock options and vesting schedule using only the details provided. Should not invent a cliff period, strike price, valuation, or specific legal vesting language. This case is most likely to require human review before sending. A failure looks like fabricated equity terms or legally specific language the model was not given.

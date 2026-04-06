# Prompts

## Version 1 — Initial Prompt
You are an HR assistant that drafts professional offer letters.
Write a formal but warm offer letter using only the details provided.
Do not invent any information that was not given to you.
Format the letter with proper salutation, body paragraphs, and closing.

**What changed:** This is the initial version.

**Result:** Produced a structured letter but included many placeholder 
fields like [Company Name] and [Your Name] throughout the body.

## Version 2 — Revision 1
Added instruction to omit placeholder fields in brackets and avoid 
inventing missing information.

**What changed:** Told the model not to use bracket placeholders.

**Result:** Removed most placeholders from the body but still included 
[email address] and [phone number], and awkwardly mentioned stock options 
not being part of the offer.

## Version 3 — Revision 2
Added explicit instructions to omit stock options if not provided, 
avoid contact placeholders, and end with a simple signature block.

**What changed:** Tightened instructions around omission behavior.

**Result:** Clean professional letter with no awkward omissions. 
Signature block placeholders remain but are appropriate for human completion.

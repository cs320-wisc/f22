Because the regular expressions will be used repeatedly, compiling them once before use with `re.compile(...)` is recommended; make sure this is done only once and not each time a new `Filing` object is created; storing the compiled regular expressions in class variables would be appropriate.

If you name your regular expressions carefully, you might find that `getattr` and `setattr` can be used to cut down on repeated code. Also, since Filing should extract all the information of interest by default, try to process all the ".html" and ".htm" documents in "docs.zip" at the start of your notebook; this will let you re-use the results multiple times.

When processing the files in "docs.zip", make sure to avoid attempting to process the directories. You might find the `filelist` attribute of a `ZipFile` helpful. It returns a list of `ZipInfo` objects, one for each file. Use the `ZipInfo`s `is_dir()` methods to check if the file is a directory, and get its path with the `filename` attribute.

Begin by implementing regular expressions to extract the following information.

- Filing date (store the result in attribute `filing_date` of a `Filing`)
- Date the filing was  accepted (store in attribute `accepted_date`)
- The state of incorporation of the filer (store it in `state_of_incorporation`)

Note: a few of the states of incorporation will not be US states.

**Hints:** Read about the non-greedy * operator (*?); it might be very helpful. 

Using "[^<]" in your regular expressions might also be useful; this will recognise any character except a "<", which is used at the beginning of a tag; "[^>]" could also be useful - it matches any character except a ">" (used at the end of a tag). Both of these might help you write more compact expressions.

Finally, look up `re.DOTALL`; it might be useful for some of the expressions.

## Extract corporate information

Write a regular expression to find the name of the filing company (note that the filing company will appear before other filers such as the legal firms hired by the filer). Store the result in the attribute `company_name` of a `Filing`.

Next, find the industry of the filing company and store it in the attribute `industry`. Note that this isn't shown for some types of filings (for example, investment prospectuses); store "unknown" if not found.

## Extract addresses

Extract the mailing address of the filing company (remember that the primary filer will be before secondary filers in the page). For this component it is not necessary to use a single regular expression; using several regular expressions and non-regex Python is acceptable here (and suggested). Store it in the attribute `address`.

**Hint:** Try to first find the tags containing the address lines (using the non-greedy * operator (*?) might make this much easier; this might also be a good place to use `re.DOTALL`), and next to extract the contents of each of those tags. Get the address by joining the lines together.

Next, find the state abbreviation in the address (remember that the state is prior to the zip code in the last line of the address). Store the result in `state_of_headquarters`. If there is no zip code in the last line, you may assume that the address is not in the US (and does not have a state); store "unknown" in this case.

US-standard zip codes are five digits, optionally followed by a dash and four digits.

Note: a few of the non-US addresses are formatted in a way which is consistent with the US format; this is expected. We could use a list of US state abbreviations to filter them out reliably, but we'll keep them, as the information might be useful.

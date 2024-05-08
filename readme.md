## Usage
### Example input
This should be a tsv file with two columns, the first column is the word in  and the second column is the word in אידיש. The file should be named `input.tsv`.

| עברית     | אידיש         |
|-----------|---------------|
| אורח־חיים | אוירעך־כאַיִם |
| אָבֿל     | אָוול         |
| אַבֿלות   | אַוויילעס     |


### Example output
The output will be a tsv file with three columns, the first column is the word in עברית, the second column is the word in אידיש, and the third column is the romanized version. The file will be named `output.tsv`.

| עברית     | אידיש         | romanized      |
|-----------|---------------|----------------|
| אורח־חיים | אוירעך־כאַיִם | אוירעח־ חאַיִם |
| אָבֿל     | אָוול         | אָבֿל          |
| אַבֿלות   | אַוויילעס     | אַבֿיילעת      |


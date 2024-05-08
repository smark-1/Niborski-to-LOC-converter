# Niborski to LOC converter
## Usage
### Example input
This should be a tsv file with two columns, the first column is the word in Hebrew and the second column is the word in Niborski. The file should be named `input.tsv`.

| Hebrew    | Niborski      |
|-----------|---------------|
| אורח־חיים | אוירעך־כאַיִם |
| אָבֿל     | אָוול         |
| אַבֿלות   | אַוויילעס     |


### Example output
The output will be a tsv file with three columns, the first column is the word in Hebrew, the second column is the word in Niborski, and the third column is the ALA-LC version. The file will be named `output.tsv`.

| Hebrew    | Niborski      | ALA-LC         |
|-----------|---------------|----------------|
| אורח־חיים | אוירעך־כאַיִם | אוירעח־ חאַיִם |
| אָבֿל     | אָוול         | אָבֿל          |
| אַבֿלות   | אַוויילעס     | אַבֿיילעת      |


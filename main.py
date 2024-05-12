import csv
import difflib

# if set to True, create an additional line with the hyphen removed
DUPLICATE_HYPHEN = True

input_file = 'input.tsv'
output_file = 'output.tsv'
conversion_rules = 'rules.tsv'


def read_file(file: str):
    """
    opens the tsv file and read the lines using utf-8 encoding so that the file can be read in any language
    :param file:
    :return: [[original, new], ...]
    """
    with open(file, encoding='utf-8') as f:
        lines = f.readlines()
    return [line.strip().split('\t') for line in lines]


# get list of all conversion rules
rules = read_file(conversion_rules)


def show_diff(seqm):
    """Unify operations between two compared string
    seqm is a difflib.SequenceMatcher instance whose a & b are strings
    if the diff is a replacement then using the rules will swap the characters
    """
    output = []
    for opcode, a0, a1, b0, b1 in seqm.get_opcodes():
        if opcode == 'equal':  # no change
            output.append(seqm.a[a0:a1])
        elif opcode == 'insert':  # new characters added
            output.append(seqm.b[b0:b1])
        elif opcode == 'delete':  # characters removed
            pass
        elif opcode == 'replace':  # characters replaced
            # get the original and changed characters
            original = seqm.a[a0:a1]
            changed = seqm.b[b0:b1]
            # apply the rules
            for rule in rules:
                # if a rule is found in the original string, check if the changed char is in the changed string, replace the change with the original string
                if rule[0] in original:
                    if rule[1] in changed:
                        changed = changed.replace(rule[1], rule[0])
            output.append(changed)
        else:
            raise RuntimeError("unexpected opcode")
    return ''.join(output)


def get_sequence(line1, line2):
    """ get the sequence of the two lines """
    seqm = difflib.SequenceMatcher(None, line1, line2)
    return seqm


# open the output file and write the results
with open(output_file, 'w', newline='', encoding='utf-8') as file:
    csvwriter = csv.writer(file, delimiter='\t')
    for i, line in enumerate(read_file(input_file)):
        try:
            print(f"{'line ' + str(i + 1):=^30}")
            print('Hebrew\t\t\t', line[0])
            print('Niborski \t\t', line[1])
            ALA_LC = show_diff(get_sequence(line[0], line[1]))
            if line[0][-1] == 'ה' and ALA_LC[-1] != 'ה':
                ALA_LC = ALA_LC + 'ה'
            print('ALA-LC\t\t\t', ALA_LC)
            # if set to True, create an additional line with the hyphen removed
            if DUPLICATE_HYPHEN:
                if '־' in ALA_LC:
                    print('ALA-LC (w/o ־) \t', ALA_LC.replace('־', ' '))
                    csvwriter.writerow([line[0].replace('־', ' '),
                                        line[1].replace('־', ' '),
                                        ALA_LC.replace('־', ' ')])
            csvwriter.writerow([line[0], line[1], ALA_LC])
        except IndexError:
            print(f"IndexError: {line} is missing a value")

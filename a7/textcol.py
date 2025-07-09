# Assignment 7, Task 5
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 4 hrs
# Use of AI: NO/YES
# AI usage details: It failed to generate test cases for me


### Your code start here ######
class TextColumn:
    def __init__(self, lines) -> None:
        self.lines = lines

    def paragraphs(self) -> list[str]:
        paragraphs_list = []
        temp = ""
        for line in self.lines:
            in_feature = False
            char_in_line = 0
            for idx in range(len(line)):

                if line[idx] == "+" or line[idx] == "|":
                    in_feature = not in_feature
                    continue

                if not in_feature:
                    char_in_line += 1

                    try:  # too lazy to clean this mess, it works though
                        if (
                            line[idx] == "-"
                            and (
                                idx == len(line) - 2 or line[idx + 1] in {"+", "|", " "}
                            )
                            and (
                                idx + 2 < len(line)
                                and line[idx + 2] in {"+", "|", "-", " "}
                            )
                        ):
                            break
                    except IndexError:
                        break

                    try:
                        if (
                            line[idx] == " " and idx == 0
                        ) or (  # "                 paragraph is approaching - notice",
                            (line[idx] == " ")
                            and (
                                line[idx - 1] == "+"
                                or line[idx - 1] == "|"
                                or line[idx - 1]
                                == " "  # "                 paragraph is approaching - notice",
                            )
                        ):
                            continue  # "+--------------+ really gained much - sorry. I am",
                    except IndexError:
                        continue  # continue anyway

                    temp = temp + line[idx]

                if idx == (len(line) - 1):
                    temp = temp + " "

            if char_in_line == 0:
                paragraphs_list.append(temp)
                temp = ""

        paragraphs_list.append(temp)

        return paragraphs_list

    def features(self) -> list[str]:
        features_lists = []
        in_box = False
        temp = ""

        for line in self.lines:
            start_feature = False
            in_in_box = False

            for idx in range(len(line)):
                if in_box:
                    if line[idx] == "+":
                        in_box = False
                        if temp.strip():
                            cleaned = ""
                            space = False
                            for ch in temp.strip():
                                if ch == " ":
                                    if not space:
                                        cleaned += " "
                                        space = True
                                else:
                                    cleaned += ch
                                    space = False

                            features_lists.append(cleaned)

                        temp = ""
                        break

                    if in_in_box:
                        if line[idx] == "|":
                            in_in_box = False
                            continue

                        if line[idx] != " ":
                            start_feature = True

                        if start_feature:
                            temp += line[idx]

                        if (
                            start_feature
                            and line[idx] == " "
                            and (line[idx + 1] == " " or line[idx + 1] == "|")
                        ):
                            start_feature = False
                            in_in_box = False
                            break
                    else:
                        if line[idx] == "|":
                            in_in_box = True
                else:
                    if line[idx] == "+":
                        in_box = True
                        break

        return features_lists


lines = [
    "This is an example piece of text. This is an exam-",
    "ple piece of text. This is an example piece of",
    "text. This is an example",
    "piece of text. This is a +-----------------------+",
    "sample for a challenge.  |                       |",
    "Lorum ipsum dolor sit a- |   top class feature   |",
    "met and other words. The |                       |",
    "proper word for a layout +-----------------------+",
    "like this would be type-",
    "setting, or so I would",
    "imagine, but for now let's carry on calling it an",
    "example piece of text. Hold up - the end of the",
    "                 paragraph is approaching - notice",
    "+--------------+ the double line break for a para-",
    "|              | graph.",
    "|              |",
    "|  feature     | And so begins the start of the",
    "|  bonanza     | second paragraph but as you can",
    "|              | see it's only marginally better",
    "|              | than the other one so you've not",
    "+--------------+ really gained much - sorry. I am",
    "                 certainly not a budding author",
    "as you can see from this example input. Perhaps I",
    "need to work on my writing skills.",
]

c = TextColumn(lines)

expected_paragraphs = [
    "This is an example piece of text. This is an example piece of text. This is an example piece of text. This is an example piece of text. This is a sample for a challenge. Lorum ipsum dolor sit amet and other words. The proper word for a layout like this would be typesetting, or so I would imagine, but for now let's carry on calling it an example piece of text. Hold up - the end of the paragraph is approaching - notice the double line break for a paragraph. ",
    "And so begins the start of the second paragraph but as you can see it's only marginally better than the other one so you've not really gained much - sorry. I am certainly not a budding author as you can see from this example input. Perhaps I need to work on my writing skills. ",
]
expected_features = ["top class feature", "feature bonanza"]

# LLM cannot generate an accurate test case result for `paragraph()`, so I checked it manually, and use mine result as a test case; just dm me, open up an issue or fix it yourself if you found any mistake -- or just ignore it
assert c.paragraphs() == expected_paragraphs

assert set(c.features()) == set(expected_features)

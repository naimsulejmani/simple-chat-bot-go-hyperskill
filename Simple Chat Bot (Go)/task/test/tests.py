import re

from hstest.stage_test import *
from hstest.test_case import TestCase

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)


class ChattyBotTest(StageTest):
    def generate(self) -> List[TestCase]:
        mary_input = "Mary\n1\n0\n5\n10\n" + '\n'.join(str(i + 1) for i in range(10))
        jeff_input = "Jeff\n2\n4\n1\n7\n" + '\n'.join(str(i + 1) for i in range(10))

        return [
            TestCase(stdin=mary_input, attach=("Mary", 40, 10)),
            TestCase(stdin=jeff_input, attach=("Jeff", 29, 7))
        ]

    def check(self, reply: str, clue: Any) -> CheckResult:
        lines = reply.strip().splitlines()

        # Previous stages common checks
        if not re.match(r"^Hello! My name is .*\.$", lines[0]):
            return CheckResult.wrong(
                "The 1-st line of your output is NOT correct.\n" +
                "Your program incorrectly output as the 1-st line: " + lines[0] + "\n\n" +
                "The 1-st line should be: 'Hello! My name is {bot_name}.'"
            )

        if not re.match(r"^I was created in \d{4}\.$", lines[1]):
            return CheckResult.wrong(
                "The 2nd line of your output does NOT match the expected format or does NOT contain a valid year.\n" +
                "Your program incorrectly output as the 2-nd line: " + lines[1] + "\n\n" +
                "The 2-nd line should be: 'I was created in {birth_year}.' "
                "where {birth_year} is a four-digit number like 2023."
            )

        if lines[2] != "Please, remind me of your name.":
            return CheckResult.wrong(
                "The 3-rd line of your output is NOT correct.\n" +
                "Your program incorrectly output as the 3-rd line: " + lines[2] + "\n\n" +
                "The 3-rd line should be: 'Please, remind me of your name.'"
            )

        line_with_name = lines[3].lower()
        name = clue[0].lower()
        name_pattern = rf"^what a great name you have, {name}!$"
        if name not in line_with_name or not re.match(name_pattern, line_with_name):
            return CheckResult.wrong(
                "The 4-th line of your output is NOT correct.\n" +
                "Your program incorrectly output as the 4-th line: " + lines[3] + "\n\n" +
                "The 4-th line should be: 'What a great name you have, {name}!' "
                "where {name} is the name you input earlier."
            )

        if lines[4] != "Let me guess your age.":
            return CheckResult.wrong(
                "The 5-th line of your output is NOT correct.\n" +
                "Your program incorrectly output as the 5-th line: " + lines[4] + "\n\n" +
                "The 5-th line should be: 'Let me guess your age.'"
            )

        if lines[5] != "Enter remainders of dividing your age by 3, 5 and 7.":
            return CheckResult.wrong(
                "The 6-th line of your output is NOT correct.\n" +
                "Your program incorrectly output as the 6-th line: " + lines[5] + "\n\n" +
                "The 6-th line should be: 'Enter remainders of dividing your age by 3, 5 and 7.'"
            )

        line_with_age = lines[6].lower()
        age = str(clue[1])
        age_pattern = rf"^your age is {age}; that's a good time to start programming!$"
        if age not in line_with_age or not re.match(age_pattern, line_with_age):
            return CheckResult.wrong(
                "The 7-th line of your output does NOT match the expected format "
                "or does NOT calculate the age correctly.\n" +
                "Your program incorrectly output as the 7-th line: " + lines[6] + "\n\n" +
                f"The 7th line should be: 'Your age is {clue[1]}; that's a good time to start programming!'"
            )

        if lines[7] != "Now I will prove to you that I can count to any number you want.":
            return CheckResult.wrong(
                "The 8-th line of your output is NOT correct.\n" +
                "Your program incorrectly output as the 8-th line: " + lines[7] + "\n\n" +
                "The 8-th line should be: 'Now I will prove to you that I can count to any number you want.'"
            )

        # Stage 4 tests
        number_pattern = r"^(\d+)( !|!)?$"  # Pattern that can match numbers in three formats: 0, 0!, or 0 !

        # Find the starting line of the number sequence output
        start_line = None
        for idx, line in enumerate(lines):
            if re.match("^0( !|!)?$", line.strip()):
                start_line = idx
                break

        if start_line is None:
            expected_sequence = '\n'.join([f"{i}!" for i in range(clue[2] + 1)])
            return CheckResult.wrong(
                "The start of the counting sequence does NOT match the expected "
                "format or was NOT found in the output.\n" +
                f"Ensure you print numbers from 0 to the input number: {clue[2]} inclusive.\n"
                f"Each number should be printed on a new line followed by an exclamation mark '!'\n\n"
                f"For example, if the input number is {clue[2]}, the expected output sequence should be:\n"
                f"{expected_sequence}"
            )

        # Check if the program did not reach the input number
        last_number_line_idx = start_line
        while re.match(number_pattern, lines[last_number_line_idx]):
            last_number_line_idx += 1
        last_number_line_idx -= 1  # Adjust to point to the actual last counting line
        last_number_line = lines[last_number_line_idx]

        match = re.match(number_pattern, last_number_line)
        if match:
            last_number = int(match.group(1))
            if last_number < clue[2]:
                return CheckResult.wrong(
                    f"Your program did NOT count up to the input number.\n" +
                    f"Expected to count from 0 to the input number: {clue[2]} "
                    f"but your program only counted up to: {last_number}"
                )

        # Check counting lines
        for i in range(clue[2] + 1):
            num_line = lines[start_line + i].strip()
            expected_pattern = f"^{i}( !|!)?$"
            if not re.match(expected_pattern, num_line):
                return CheckResult.wrong(
                    f"The {start_line + i + 1}-th line of your output is NOT correct.\n" +
                    f"Your program incorrectly output as the {start_line + i + 1}-th line: " + num_line + "\n\n" +
                    f"The {start_line + i + 1}-th line should be one of: '{i}', '{i}!', or '{i} !'"
                )

        # Check if the program counts past the input number
        if re.match(number_pattern, lines[start_line + clue[2] + 1]):
            return CheckResult.wrong(
                "Your program counted and printed more numbers than expected.\n" +
                f"Expected to count from 0 to the input number: {clue[2]} "
                f"but your program counted past that number until: {re.match(number_pattern, lines[-2]).group(0)}"
            )

        # Stage 5 tests
        # After the counting, the next line should introduce the programming question
        question_intro_idx = lines.index(last_number_line) + 1
        if lines[question_intro_idx] != "Let's test your programming knowledge.":
            return CheckResult.wrong(
                f"The {question_intro_idx + 1}-th line of your output is NOT correct.\n" +
                f"Your program incorrectly output "
                f"as the {question_intro_idx + 1}-th line: " + lines[question_intro_idx] + "\n\n" +
                f"The {question_intro_idx + 1}-th line should be: 'Let's test your programming knowledge.'"
            )

        # Locate the question
        question_line_idx = question_intro_idx + 1
        if not lines[question_line_idx].endswith("?"):
            return CheckResult.wrong(
                "Expected a programming-related question ending with a '?', but found: " + lines[question_line_idx]
            )

        # Check multiple-choice answers
        options_count = 0
        idx = question_line_idx + 1
        while idx < len(lines) and re.match(r"^\d+\.", lines[idx]):
            options_count += 1
            idx += 1

        if options_count < 2:
            return CheckResult.wrong(
                "Your multiple-choice answers are less than 2. Please provide at least 2 options."
            )

        # Check if the bot prompts for incorrect answers
        if "Please, try again." not in lines:
            return CheckResult.wrong(
                "Your bot should prompt the user with 'Please, try again.' for an incorrect answer."
            )

        # Check the last line
        if lines[-1] != "Congratulations, have a nice day!" and lines[-1] != "Completed, have a nice day!":
            return CheckResult.wrong(
                "The last line of your output is NOT correct.\n" +
                f"Your program incorrectly output as the last line: '{lines[-1]}'\n\n"
                f"Ensure your program is correctly counting from 0 to the input number: {clue[2]}\n"
                f"and that the last line of your program is: 'Congratulations, have a nice day!'"
            )

        return CheckResult.correct()


if __name__ == '__main__':
    ChattyBotTest().run_tests()

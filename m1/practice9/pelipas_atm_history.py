def view_history():
    try:
        with open("transactions.txt", "r") as file:
            lines = file.readlines()

        return lines

    except FileNotFoundError:
        return []


######### Learning Signature #########
# Programmed by: Hariette Claire M. Pelipas
# Date Submitted: September 3, 2026
#
# Program Description: This program reads the transaction history from transactions.txt and returns the transaction lines to the main program.
# Reflection: I learned how to read data from a text file and return the lines to another program. I also learned how to handle FileNotFoundError when the transaction file does not exist.
#
# AI Usage
# [/] No AI Assistance – Completed independently without AI.
# [ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
# [ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
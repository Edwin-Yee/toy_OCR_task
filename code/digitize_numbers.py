from PIL import Image
import pytesseract

output_file = 'output.txt'

correct, incorrect = 0, 0
number_uncertain = 0
ground_truth = ["1890", "29", "25", "48", "-100.0", "11", "8", "15", "1901", "26", "127", "43", "12", "3", "31", 
                "12", "1895", ".66", "4.16", "17", "40", "119", "12", "10", "1902", "64", "60", "6", "27", "1902"]

with open(output_file, 'w') as out_file:
    for i in range(1, 31):
        image_path = f'../data/image_{i}.png'

        # default tesseract: Accuracy:0.8421052631578947
        # oem3, psm7 tesseract: Accuracy: 0.90
        # fix hyphen -> negative sign, oem3, psm7 tesseract: Accuracy: 0.9333333333333333

        try:
            custom_oem_psm_config = r'--oem 3 --psm 7'
            number = pytesseract.image_to_string(image_path, timeout=20, config=custom_oem_psm_config)

        except RuntimeError as timeout_error:
            # Tesseract processing is terminated
            pass
        
        if number:
            # complete preprocessing, strip right spaces, replaces hyphen with minus sign
            number = number.rstrip()
            if number[0] == "—":
                number = "-" + number[1:]

            if number == ground_truth[i-1]:
                correct += 1
            else:
                print(f"Incorrect: {number} vs {ground_truth[i-1]} at index {i}")
                incorrect += 1

            out_file.write(f'{number}\n')
        else:
            out_file.write(f'Uncertain for index i: {i}\n')
            number_uncertain += 1
        

print("Uncertain values:" + str(number_uncertain))
print("Number evaluated:" + str(correct + incorrect))
print("Accuracy:" + str(correct / (correct + incorrect)))

import re
import unittest
import os

# Import your custom function from 'getAllFiles_runs.py'
from getAllFiles_runs import getAllFiles_in_run

# Call the function to get a list of files
allrunfiles = getAllFiles_in_run()

# Create a list to store individual test results
individual_test_results = []

# Track the overall test result
overall_test_passed = True

# Loop through each file in the list
for filez in allrunfiles:
    # Convert backslashes to forward slashes for file path compatibility
    python_file_path = filez.replace('\\', '/')
    print(python_file_path)  # Print the file path

    # Extract chapter number and name from the file path
    x = python_file_path.split('/')
    chapter_number = x[2]
    chapter_name = x[3]
    print(chapter_name)
    print(chapter_number)

    if chapter_name:
        # Generate the test file path based on chapter information
        test_file_path = f'Tests_Final/{chapter_number}/test_{chapter_name}.py'
        print(test_file_path)

        # Define the output test file path where combined content will be saved
        output_test_file_path = 'combined_test.py'  # Change this to the desired output file path

        # Read the content of the Python file
        with open(python_file_path, 'r') as python_file:
            python_content = python_file.read()

        # Read the content of the test file
        with open(test_file_path, 'r', encoding='utf-8') as test_file:
            test_content = test_file.read()
            # Split the content into lines
            lines = test_content.split('\n')

            # Filter out lines that contain "from ch13"
            filtered_lines = [line for line in lines if "from ch" not in line]

            # Join the filtered lines back into a single string
            filtered_content = '\n'.join(filtered_lines)
            test_content = filtered_content

        # Combine the content of the two files
        combined_content = "\nimport unittest\n" + python_content+"\n" + test_content

        # Write the combined content to a new file
        with open(output_test_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(combined_content)

        # Import and run tests from the new file
        import importlib.util

        spec = importlib.util.spec_from_file_location("combined_test", output_test_file_path)
        combined_test_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(combined_test_module)

        # Load and run the tests from the new module
        test_loader = unittest.TestLoader()
        test_suite = test_loader.loadTestsFromModule(combined_test_module)
        test_runner = unittest.TextTestRunner()
        test_result = test_runner.run(test_suite)

        # Calculate tests passed and total tests
        tests_passed = test_result.testsRun - len(test_result.failures) - len(test_result.errors)
        total_tests = test_result.testsRun
       
        #extract mutation
        pattern = r'mutation_(\S+)'
        # Use re.search to find the first match
        match = re.search(pattern, python_file_path)
        # Create the full path for the new Python file with .py extension
        new_filename = match.group(0)    
        # Store individual test result in a list
           # Append the individual test result
        if tests_passed == total_tests:
            individual_test_results.append(f"{new_filename}--yes--{tests_passed}--{total_tests}")
        else:
            individual_test_results.append(f"{new_filename}--no--{tests_passed}--{total_tests}")

        # Check if the current test result is successful
        if not test_result.wasSuccessful():
            overall_test_passed = False

# Write the individual test results to a text file
with open('test_results_run_3.txt', 'w') as result_file:
    for result in individual_test_results:
        result_file.write(result + '\n')

# Check the overall test result
if overall_test_passed:
    print("All tests passed!")
else:
    print("Some tests failed.")

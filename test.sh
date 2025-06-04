#!/bin/sh
# Q Dev App Test Suite

echo "Starting Q Dev App tests..."

# Test 1: Check if required tools are installed
echo "Test 1: Checking required tools..."
for tool in python3 pip curl jq bash; do
    if command -v $tool > /dev/null 2>&1; then
        echo "✓ $tool is installed"
    else
        echo "✗ $tool is NOT installed"
        exit 1
    fi
done

# Test 2: Check Python version
echo "Test 2: Checking Python version..."
python_version=$(python3 --version)
echo "Python version: $python_version"

# Test 3: Simple functionality test
echo "Test 3: Running functionality test..."
echo "Hello, Q Dev App!" > test_output.txt
if grep -q "Hello, Q Dev App!" test_output.txt; then
    echo "✓ File I/O test passed"
else
    echo "✗ File I/O test failed"
    exit 1
fi

# Test 4: README.md summary functionality
echo "Test 4: Testing README.md summary functionality..."
python3 app.py --summarize-readme > readme_summary.txt
if grep -q "Q Dev App" readme_summary.txt && grep -q "Key Features:" readme_summary.txt; then
    echo "✓ README.md summary functionality test passed"
else
    echo "✗ README.md summary functionality test failed"
    exit 1
fi

# Clean up
rm test_output.txt readme_summary.txt

echo "All tests passed successfully!"
exit 0
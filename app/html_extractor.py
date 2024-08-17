from bs4 import BeautifulSoup
import re

def extract_html(text):
    """
    Extract HTML content from a given text.
    
    Args:
    text (str): Input text that may contain HTML.
    
    Returns:
    str: Extracted HTML content, or empty string if no HTML found.
    """
    # First, try to find content between ```html and ``` tags
    match = re.search(r'```html\s*(.*?)\s*```', text, re.DOTALL)
    if match:
        html_content = match.group(1)
    else:
        # If not found, look for any content that looks like HTML
        html_pattern = r'<\s*html[^>]*>.*?<\s*/\s*html\s*>'
        match = re.search(html_pattern, text, re.DOTALL | re.IGNORECASE)
        if match:
            html_content = match.group(0)
        else:
            # If still not found, check for any HTML-like content
            html_like_pattern = r'<[^>]+>.*?</[^>]+>'
            match = re.search(html_like_pattern, text, re.DOTALL)
            if match:
                html_content = match.group(0)
            else:
                return ""
    
    # Parse and prettify the HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.prettify()

# Unit tests
import unittest

class TestExtractHTML(unittest.TestCase):
    
    def test_html_in_code_block(self):
        input_text = '''
        Some text before
        ```Sure following is your outpub 
        fsdf sdf
        <html><body><h1>Test</h1></body></html>
        ```
        Some text after
        '''
        expected_output = '''
<html>
 <body>
  <h1>
   Test
  </h1>
 </body>
</html>
'''.strip()
        self.assertEqual(extract_html(input_text).strip(), expected_output)
    
    def test_html_without_code_block(self):
        input_text = '''
        Some text before
        <html><body><h1>Test</h1></body></html>
        Some text after
        '''
        expected_output = '''
<html>
 <body>
  <h1>
   Test
  </h1>
 </body>
</html>
'''.strip()
        self.assertEqual(extract_html(input_text).strip(), expected_output)
    
    def test_partial_html(self):
        input_text = '''
        Some text before
        <div><p>This is a paragraph</p></div>
        Some text after
        '''
        expected_output = '''
<div>
 <p>
  This is a paragraph
 </p>
</div>
'''.strip()
        self.assertEqual(extract_html(input_text).strip(), expected_output)
    
    def test_no_html(self):
        input_text = "This is just plain text"
        self.assertEqual(extract_html(input_text), "")
    
    def test_multiple_html_blocks(self):
        input_text = '''
        <html><body><h1>First</h1></body></html>
        Some text in between
        <html><body><h1>Second</h1></body></html>
        '''
        expected_output = '''
<html>
 <body>
  <h1>
   First
  </h1>
 </body>
</html>
'''.strip()
        self.assertEqual(extract_html(input_text).strip(), expected_output)
    
    def test_malformed_html(self):
        input_text = '<html><body><h1>Malformed'
        expected_output = '''
<html>
 <body>
  <h1>
   Malformed
  </h1>
 </body>
</html>
'''.strip()
        self.assertEqual(extract_html(input_text).strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
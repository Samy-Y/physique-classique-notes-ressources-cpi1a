import sys
import gh_md_to_html

def convert_markdown_to_html(input_file, output_file=None):
    """
    Convert a markdown file to HTML using gh-md-to-html.
    
    Args:
        input_file: Path to the markdown file
        output_file: Path for the output HTML file (optional)
    """
    if output_file is None:
        output_file = input_file.rsplit('.', 1)[0] + '.html'
    
    gh_md_to_html.main(input_file, destination=output_file, origin_type="file")
    print(f"Converted {input_file} to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python conversion.py <input.md> [output.html]")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    convert_markdown_to_html(input_path, output_path)
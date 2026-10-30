#!/usr/bin/env python3
import os
import re

def md_to_html(md_text):
    """Converts a block of markdown text into clean HTML."""
    lines = md_text.split('\n')
    html_out = []
    in_list = None # 'ul', 'ol', or None
    in_table = False
    table_headers = []
    table_rows = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # 1. Handle code blocks
        if stripped.startswith('```'):
            if in_list:
                html_out.append(f"</{in_list}>")
                in_list = None
            if in_table:
                html_out.append(render_table(table_headers, table_rows))
                in_table = False
                
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1
            code_text = '\n'.join(code_lines)
            html_out.append(f"<pre>{code_text}</pre>")
            i += 1
            continue
            
        # 2. Handle Tables
        if stripped.startswith('|'):
            if in_list:
                html_out.append(f"</{in_list}>")
                in_list = None
            
            # Skip separator rows like | --- | --- |
            if re.match(r'^\|[\s:-|]+$', stripped):
                i += 1
                continue
                
            cols = [c.strip() for c in stripped.split('|')[1:-1]]
            if not in_table:
                in_table = True
                table_headers = cols
                table_rows = []
            else:
                table_rows.append(cols)
            i += 1
            continue
        elif in_table:
            # Table ended, render it
            html_out.append(render_table(table_headers, table_rows))
            in_table = False
            table_headers = []
            table_rows = []

        # 3. Handle Lists
        if stripped.startswith('* ') or stripped.startswith('- '):
            if in_list == 'ol':
                html_out.append("</ol>")
                in_list = None
            if not in_list:
                html_out.append("<ul>")
                in_list = 'ul'
            content = format_inline(stripped[2:])
            html_out.append(f"<li>{content}</li>")
            i += 1
            continue
        elif re.match(r'^\d+\.\s', stripped):
            if in_list == 'ul':
                html_out.append("</ul>")
                in_list = None
            if not in_list:
                html_out.append("<ol>")
                in_list = 'ol'
            match = re.match(r'^(\d+)\.\s(.*)', stripped)
            content = format_inline(match.group(2))
            html_out.append(f"<li>{content}</li>")
            i += 1
            continue
        else:
            if in_list:
                html_out.append(f"</{in_list}>")
                in_list = None

        if not stripped:
            i += 1
            continue

        # 4. Handle Headings
        if stripped.startswith('# '):
            content = format_inline(stripped[2:])
            html_out.append(f"<h1>{content}</h1>")
        elif stripped.startswith('## '):
            content = format_inline(stripped[3:])
            html_out.append(f"<h2>{content}</h2>")
        elif stripped.startswith('### '):
            content = format_inline(stripped[4:])
            html_out.append(f"<h3>{content}</h3>")
        elif stripped.startswith('#### '):
            content = format_inline(stripped[5:])
            html_out.append(f"<h4>{content}</h4>")
            
        # 5. Handle Images
        elif stripped.startswith('![') and '](' in stripped:
            match = re.match(r'!\[(.*?)\]\((.*?)\)', stripped)
            if match:
                alt_text = match.group(1)
                img_path = match.group(2)
                html_out.append(f'<div class="board-image-container"><img src="{img_path}" alt="{alt_text}"></div>')
            else:
                html_out.append(f"<p>{format_inline(stripped)}</p>")
                
        # 6. Standard Paragraphs
        else:
            html_out.append(f"<p>{format_inline(stripped)}</p>")
            
        i += 1
        
    if in_list:
        html_out.append(f"</{in_list}>")
    if in_table:
        html_out.append(render_table(table_headers, table_rows))
        
    return '\n'.join(html_out)

def format_inline(text):
    """Formats bold and italic inline styles in markdown text."""
    # Convert bold **text** to <strong>text</strong>
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    # Convert italic *text* to <em>text</em>
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    return text

def render_table(headers, rows):
    """Renders HTML table from header and row list."""
    out = ["<table>", "<thead>", "<tr>"]
    for h in headers:
        out.append(f"<th>{format_inline(h)}</th>")
    out.append("</tr>")
    out.append("</thead>")
    out.append("<tbody>")
    for r in rows:
        out.append("tr" if not out else "<tr>")
        for cell in r:
            out.append(f"<td>{format_inline(cell)}</td>")
        out.append("</tr>")
    out.append("</tbody>")
    out.append("</table>")
    return '\n'.join(out)

def split_markdown_into_pages(html_text, scenario_num):
    """Splits scenario HTML into A4 pages based on content sizing for print-to-pdf."""
    lines = html_text.split('\n')
    pages = []
    current_page = []
    
    # We will split pages at reasonable thresholds to keep presentation clean
    if scenario_num == 1:
        # Scenario 1 has 3 A4 pages of text
        # Page 1: Title, Executive Summary, Prompts
        # Page 2: BOM Table, Mechanical Connections
        # Page 3: Passivhaus Engineering, AI Reflection
        p1 = []
        p2 = []
        p3 = []
        dest = p1
        for line in lines:
            if "### 1.3" in line or "### 1.4" in line:
                dest = p2
            elif "### 1.5" in line or "### 1.6" in line:
                dest = p3
            dest.append(line)
        pages.append('\n'.join(p1))
        pages.append('\n'.join(p2))
        pages.append('\n'.join(p3))
        
    elif scenario_num == 2:
        # Scenario 2 has 3 pages
        # Page 1: Title, Prompts, LCA Goals & Scope (steps 1-6)
        # Page 2: Earthmoving Machinery & WSUD (steps 7-11), Standards Table
        # Page 3: Equipment Spec Matrix, Workforce recommendations, Critical reflection
        p1 = []
        p2 = []
        p3 = []
        dest = p1
        for line in lines:
            if "7. Earthmoving Machinery Recommendations" in line or "Item | Data / Standard Used" in line:
                dest = p2
            elif "### 2.3" in line or "### 2.4" in line or "### 2.5" in line:
                dest = p3
            dest.append(line)
        pages.append('\n'.join(p1))
        pages.append('\n'.join(p2))
        pages.append('\n'.join(p3))
        
    elif scenario_num == 3:
        # Scenario 3 has 2 pages
        # Page 1: Title, Prompts, Mix Design Plan (sections 3.1 - 3.2.3)
        # Page 2: Pavement Table, Traffic Signal AI, Trade-off Matrix, Critique
        p1 = []
        p2 = []
        dest = p1
        for line in lines:
            if "Pavement cross-section, surface to subgrade:" in line or "### 3.3" in line or "### 3.4" in line:
                dest = p2
            dest.append(line)
        pages.append('\n'.join(p1))
        pages.append('\n'.join(p2))
        
    return pages

def main():
    if not os.path.exists("master_report.md"):
        print("Error: master_report.md not found.")
        return
        
    print("Reading master_report.md...")
    with open("master_report.md", "r", encoding="utf-8") as f:
        md_text = f.read()

    # Split markdown by Scenario headings using regex to avoid splitting on intermediate # headings
    import re
    s1_match = re.search(r'(# 1\. Scenario 1[\s\S]*?)(?=# 2\. Scenario 2)', md_text)
    s2_match = re.search(r'(# 2\. Scenario 2[\s\S]*?)(?=# 3\. Scenario 3)', md_text)
    s3_match = re.search(r'(# 3\. Scenario 3[\s\S]*)', md_text)
    
    s1_md = s1_match.group(1) if s1_match else ""
    s2_md = s2_match.group(1) if s2_match else ""
    s3_md = s3_match.group(1) if s3_match else ""

    # Render each markdown block to HTML
    s1_html = md_to_html(s1_md)
    s2_html = md_to_html(s2_md)
    s3_html = md_to_html(s3_md)

    # Split into pages
    s1_pages = split_markdown_into_pages(s1_html, 1)
    s2_pages = split_markdown_into_pages(s2_html, 2)
    s3_pages = split_markdown_into_pages(s3_html, 3)

    # Read original master_report.html
    if not os.path.exists("master_report.html"):
        print("Error: master_report.html not found.")
        return
        
    with open("master_report.html", "r", encoding="utf-8") as f:
        html_content = f.read()

    # Extract head (everything up to <body>)
    body_match = re.search(r'([\s\S]*?<body[\s\S]*?>[\s\S]*?<!-- COVER PAGE -->[\s\S]*?<!-- TABLE OF CONTENTS -->[\s\S]*?</div>)', html_content)
    if not body_match:
        print("Error: Could not parse head and cover/TOC from master_report.html")
        return
    head_and_toc = body_match.group(1)

    # Extract A3 board layout
    board_match = re.search(r'(<!-- SCENARIO 1: A3 ARCHITECTURAL BOARD -->[\s\S]*?<!-- Architectural Title Block -->[\s\S]*?</div>\s*</div>\s*</div>)', html_content)
    if not board_match:
        print("Error: Could not parse A3 architectural board from master_report.html")
        # Let's search with a slightly wider regex
        board_match = re.search(r'(<!-- SCENARIO 1: A3 ARCHITECTURAL BOARD -->[\s\S]*?<!-- Architectural Title Block -->[\s\S]*?</div>\s*</div>\s*</div>)', html_content)
        if not board_match:
            # Revert to a fallback
            board_match = re.search(r'(<div class="a3-board-page"[\s\S]*?<!-- Architectural Title Block -->[\s\S]*?</div>\s*</div>\s*</div>)', html_content)
            if not board_match:
                # Even wider
                board_match = re.search(r'(<div class="a3-board-page"[\s\S]*?</div>\s*</div>)', html_content)
                if not board_match:
                    print("Error: Fatal - could not isolate A3 board")
                    return
    
    board_html = board_match.group(1)
    if not board_html.strip().startswith('<!-- SCENARIO 1: A3 ARCHITECTURAL BOARD -->'):
        board_html = '    <!-- SCENARIO 1: A3 ARCHITECTURAL BOARD -->\n    ' + board_html

    # Assemble HTML
    new_html_parts = [head_and_toc]
    
    # Add Scenario 1 A4 pages
    for idx, p in enumerate(s1_pages):
        new_html_parts.append(f'\n    <!-- SCENARIO 1 REPORT PAGE {idx+1} -->\n    <div class="page">\n{p}\n    </div>')
        
    # Add A3 board
    new_html_parts.append(board_html)
    
    # Add Scenario 2 A4 pages
    for idx, p in enumerate(s2_pages):
        new_html_parts.append(f'\n    <!-- SCENARIO 2 PAGE {idx+1} -->\n    <div class="page">\n{p}\n    </div>')
        
    # Add Scenario 3 A4 pages
    for idx, p in enumerate(s3_pages):
        new_html_parts.append(f'\n    <!-- SCENARIO 3 PAGE {idx+1} -->\n    <div class="page">\n{p}\n    </div>')
        
    new_html_parts.append('\n</body>\n</html>')
    
    final_html = '\n'.join(new_html_parts)
    
    # Write to master_report.html
    with open("master_report.html", "w", encoding="utf-8") as f:
        f.write(final_html)
        
    print("Success! Regenerated master_report.html from master_report.md.")

if __name__ == "__main__":
    main()

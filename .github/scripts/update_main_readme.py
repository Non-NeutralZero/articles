#!/usr/bin/env python3
import os
import glob
import re

def get_article_folders():
    """Find all article folders following the pattern 'article-*'"""
    article_folders = sorted(glob.glob("article-*"))
    return article_folders

def get_article_info(folder):
    """Extract article information from the folder's README.md"""
    title = ""
    description = ""
    readme_path = os.path.join(folder, "README.md")

    if os.path.exists(readme_path):
        try:
            with open(readme_path, "r") as f:
                content = f.read()
                title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
                if title_match:
                    title = title_match.group(1).strip()
                else:
                    title = folder.replace("article-", "").replace("-", " ").title()

                title_pos = content.find("# " + title) if title else -1
                content_after_title = content[title_pos + len("# " + title):].strip()
                first_para_end = content_after_title.find("\n\n")
                if first_para_end > 0 :
                     description = content_after_title[:first_para_end].strip()
                else :
                  description = content_after_title.strip()

        except Exception as e:
            print(f"Error reading README for {folder}: {e}")



    return {
        "folder": folder,
        "title": title,
        "description": description,
        }

def generate_readme_content(articles):
    """Generate the main README.md based on the articles"""
    content = """# Articles

Articles and technical deep dives on machine learning and deep learning

"""
    
    for article in articles:
        title= article["title"]
        folder= article["folder"]
        description= article["description"]
        content+= f"## {title}\n"
        article_link = f"https://non-neutralzero.github.io/articles/{folder}/"
        github_link = f"https://github.com/Non-NeutralZero/articles/tree/main/{folder}"
        
        content+= f"[[Article]]({article_link}) [[Github]]({github_link}) \n\n"
        
        if description:
            content+= f"{description}\n"
        
        content+= "\n"
    
    return content

def update_readme(content):
    with open("README.md", "w") as f:
        f.write(content)

def main():
    article_folders = get_article_folders()
    articles = [get_article_info(folder) for folder in article_folders]
    readme_content = generate_readme_content(articles)
    update_readme(readme_content)
    print(f"README.md updated with {len(articles)} articles")

if __name__ == "__main__":
    main()

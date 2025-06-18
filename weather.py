from requests_html import HTMLSession

def weather():
    try:
        s = HTMLSession()
        query = "Guntur"
        url = f'https://www.google.com/search?q=weather+in+{query}'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}
        
        r = s.get(url, headers=headers)
        r.raise_for_status()  # Check for HTTP request errors
        
        temp = r.html.find('span#wob_tm', first=True)
        unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True)
        desc = r.html.find('span#wob_dc', first=True)
        
        # Safely access .text by checking if the element exists
        temp_text = temp.text if temp else "N/A"
        unit_text = unit.text if unit else "N/A"
        desc_text = desc.text if desc else "N/A"
        
        return f"{temp_text} {unit_text} {desc_text}"
    
    except Exception as e:
        return f"An error occurred: {e}"



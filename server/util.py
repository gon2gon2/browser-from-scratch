def show(body):
    in_tag = False
    for c in body:
        if c == "<":
            in_tag=True
        elif c == ">":
            in_tag=False
        elif not in_tag:
            print(c, end="")
            
def load(url):
    body = url.request()
    show(body)

    

        
def build_header(headers, close):
    header_string = ""
    for k,v in headers.items():
        header_string += f"{k}: {v}"
        header_string += close
        
    header_string += close
    return header_string

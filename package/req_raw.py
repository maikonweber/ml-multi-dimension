import requests
import pandas as pd
import io

def req_raw(raw):
    r = requests.get(raw)
    print(r.status_code)    
    data = r.content.decode('utf-8')
    df = pd.read_csv(io.StringIO(data))
    
    return df


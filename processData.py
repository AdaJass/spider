import asyncio
from pyquery import PyQuery as pq
import config

global n
n=0

async def processData(data,session):
    '''
    data is from the http response in main module.
    '''
    head ='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd='+data['main']
    mid ='&oq='+data['helper']
    tail ='&rsv_pq=9bc4656e000052da&rsv_t=4ccdJn1Xwirq5mlRPDl5gGVL6MXn6pNUusRxjuuY0BSrYbZ6B6FC0hayuDM&rsv_enter=0&rsv_sug3=22&rsv_sug4=1039&rsv_sug=2'
    url=head+mid+tail
    global n
    n=n+1
    print(n)
    async with session.get(url) as r:
        if n%50 == 0:
            r= await r.text(encoding='utf-8')
            with open('second.html','w', encoding='utf-8') as f: 
                f.write(r)
            


import aiohttp
import asyncio
import config
import processData as pd
import sys

async def fetchData(url, callback = pd.processData, params=None):
    #set request url and parameters here or you can pass from outside. 
    
    #use s.** request a webside will keep-alive the connection automaticaly,
    #so you can set multi request here without close the connection 
    #while in the same domain.
    #i.e. 
    #await s.get('***/page1')
    #await s.get('***/page2')
    ########################################################################        
    data={'main':sys.argv[1], 'helper': sys.argv[2]}
    while  True:
        conn = aiohttp.TCPConnector(limit=config.REQ_AMOUNTS)    
        s = aiohttp.ClientSession(headers = config.HEADERS, connector=conn)
        
        async with s.get(url, params = params) as r:    
            #here the conection closed automaticly.
            if pd.n%50 == 0:
                r= await r.text(encoding='utf-8')
                with open('first.html','w', encoding='utf-8') as f:
                    f.write(r)
            # await asyncio.sleep(1)
            await callback(data, s)

if __name__ == '__main__':
    assert(len(sys.argv)==3)
    loop = asyncio.get_event_loop()
    head = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd='+sys.argv[2]
    params = '&rsv_pq=b68f99c7000054ef&rsv_t=8f90okKQiOsUmusgx%2FiE8pOoZQ7xDdTBFGAUwbBVLwYb9uEhLOGL6Ydtx2M&rsv_enter=1&rsv_sug3=21&rsv_sug1=25&rsv_sug7=100&rsv_sug2=0&inputT=12129&rsv_sug4=12314&rsv_sug=2'
    url=head+params
    #coroutine in tasks will run 
    tasks = [fetchData(url, pd.processData) for i in range(15)]    
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close() 

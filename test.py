import requests
import random
cookie = {'cookie':'tvfe_boss_uuid=0067031f30c25219; pgv_pvid=2190174278; pgv_pvi=3051673600; pt2gguin=o0605826153; RK=iFAVYduwaS; ptcz=a52cd19508b355ecf2c8676ab3c2d93b9e79650bd56f9fbd5479dfde45514647; ua_id=RfYOjc94WOzc4xPBAAAAAL5BH5fzhcSkqpHGMQuSPiw=; mm_lang=zh_CN; pgv_si=s7406848000; cert=UL0kfUM_QPjGVOiPSMbN2dsbCuGYBN5l; noticeLoginFlag=1; uuid=8b4951e07e423698faa081a5910fa465; bizuin=3527996008; ticket=a602c697e4dadffb1c632126eff127d18da2cd25; ticket_id=gh_7ea015efae34; data_bizuin=3527996008; data_ticket=OCpHCSdogUrwOfGwkc3Qgb02KR0uI9YFA+4j2oguq/D2ynAbrunoQvdLOgBWr11d; slave_sid=Skp6MWtja3g0Rkw1dGd3cV9xVVcyTkk2VDF5T2xEOFA3bVc1Q0JYYk5jV05ZQXhpaGZURW1Ec3o1WlRtT1BjNnJTYWN6UFhMa0xQa1pac3hrZlByUWU3WlcxcGY2VkFpYlQ2Z3Z5ME14MmpVUU5PRUxORVRJSVpkZVNCa0M1c2YxTVFkd3RvMTZSM0Viazg2; slave_user=gh_7ea015efae34; xid=0726e9b0e95559e72641637b0f6f4b6d; openid2ticket_oaPJI0u0IsQy_DDhES7OyWVFOSho=wvEtE6qn/nlxdCpJWqutMWmDKrpUFjobwl5gIuaK2TU=; rewardsn=; wxtokenkey=777'}
link = 'https://mp.weixin.qq.com/cgi-bin/searchbiz?'
query_id = {'action':'search_biz','token':'197675448','lang':'zh_CN','f':'json','ajax':'1','random':random.random(),'query':'newsxinhua','begin':'0','count':'5'}
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
#输出fakeid
response = requests.get(link,params=query_id,cookies=cookie,headers=header)
print(response.text)

#输出文章链接
links = 'https://mp.weixin.qq.com/cgi-bin/appmsg?'
query_string = {'token':'197675447','lang':'zh_CN','f':'json','ajax':'1','random':random.random(),'action':'list_ex','begin':'0','count':'5','query':'','fakeid':'MzA4MjQxNjQzMA==','type':'9'}
response = requests.get(links,params=query_string,headers=header,cookies=cookie)
print(response.text)


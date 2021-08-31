from bs4 import BeautifulSoup


if __name__ == "__main__":
    html='''
    <table class="stable">
      <tbody>
            <tr class="huise">
            <td>4</td>
            <td>
                <a target="_blank" href="http://xm.gotohui.com" >厦门</a>
            </td>
            <td>50,180</td>
            <td class="red">+3.81%</td>
            <td class="red">+10.08%</td><td>36.97</td>
            </tr>
              </tbody>
</table>
    '''
    s='12,34'
    ss=s.replace(',','')
    print(ss)
    a=int(ss)
    print(a)
    soup=BeautifulSoup(html,"html.parser")
    #print(soup.prettify())
    cs=soup.find_all('tr')
    for i in cs:
        #print(i)
        city=i.find('a')
        prices=i.find_all('td')
        price=prices[2]
        print(city.text,"\t",price.text)
        #input("STOP")
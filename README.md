# SirinHostsEditor
在ipaddress.com中查询某域名所指向的IP并写入hosts或特定文件中，用于快捷解决github DNS污染等问题  

# UPDATE LOG 2.0.0  2021-10-4
[+]新增开关功能，提供以下选项，详细帮助见下  
srndas <Target Domain Name>/[-h]/[-b]/[-r] [-w [FILENAME]]/[-e]/[-l]  
    -h --help       显示帮助  
    -b --backup     备份当前/etc/hosts文件  
    -r --restore    使用备份文件还原/etc/hosts（默认于~/.sirin/bkup/srndas/）  
    -w --write      将结果写入指定文件中（默认写入到/etc/hosts，该操作需要root权限）  
    -l --load       其他操作完成后强制系统重新加载/etc/hosts文件

[^]Backup备份/Restore还原  
    将当前/etc/hosts内容备份至~/.sirin/bkup/srndas/目录下  
    可使用-r或--restore开关来进行还原  
  
[^]Write写入  
    将查询结果写入至指定文件中，若留空则写入/etc/hosts中（需要root权限），此时若有多个结果则需要进行选择  
  
[^]Load  
    >计划于2.0.1版本完成<  
  
[~]将参数调用由sys.argv改为getopt模块  
  
# UPDATE LOG 1.2.0  2021-9-2  
[~]解析库更新为lxml  
  
# UPDATE LOG 1.1.1  2021-8-20  
[~]ipaddress.com策略更新  
  
# UPDATE LOG 1.1.0  2021-8-5  
[~]爬虫内核由BeautifulSoup3更新至BeautifulSoup4  
  
# UPDATE LOG 1.0.0  2021-8-1  
[+]错误捕获机制完善，较稳定  
srndas <Target Domain Name>  
在控制台输出查询情况  
  
# UPDATE LOG A0.9.0  2021-7-25  
[+]支持同时查询IPv6  
  
# UPDATE LOG A0.8.0 2021-7-10  
[~]优化输出内容格式  
  
# UPDATE LOG A0.7.1 2021-7-3  
[~]由于'.com.cn'等顶级域名会产生区分问题，暂时只支持'.com'类型的域名  
# UPDATE LOG A0.7.0 2021-7-2  
[+]支持二级域名查询  

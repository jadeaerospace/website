import sys, html
root = sys.argv[1]

ARROW = '<svg viewBox="0 0 14 14" aria-hidden="true"><path d="M1 7h11M8 3l4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>'
DOWN = '<svg viewBox="0 0 14 14" aria-hidden="true"><path d="M7 1v11M3 8l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>'
TARGET = '''<svg class="target" viewBox="0 0 64 64" aria-hidden="true"><g fill="none" stroke="#51BAC1" stroke-width="1"><rect x="8" y="8" width="48" height="48"/><rect x="20" y="20" width="24" height="24"/><path d="M32 2v14M32 48v14M2 32h14M48 32h14"/></g><rect x="28" y="28" width="8" height="8" fill="#F6CDB4"/></svg>'''

T = {
'en': dict(
  lang='en', p='', other='zh/', otherlabel='中文', otherhreflang='zh-Hans',
  title='Jade Aerospace | Satellites, ground stations and AI for Earth observation',
  desc='Jade Aerospace is a Hong Kong company building a full Earth observation chain: a 216-satellite constellation, licensed ground stations in Brazil, a calibration field and AI analysis.',
  ogdesc='Satellites, ground stations and AI, from orbit to the field.',
  skip='Skip to content', themeLabel='Switch light / dark',
  nav=[('orbit','Constellation'),('ground','Ground stations'),('field','AgriEasy'),('proof','Work'),('team','Team')],
  contact='Contact',
  rail=[('orbit','Orbit'),('ground','Ground'),('calibration','Calibration'),('field','Field'),('proof','Proof'),('timeline','Timeline'),('team','Team'),('contact','Contact')],
  railLabel='Sections',
  sceneL='Jade Aerospace · Earth observation', sceneR='Optical scene · irrigated farmland',
  h1='From orbit<br>to the field.',
  lede='Jade Aerospace is building the whole Earth observation chain: a 216-satellite constellation, licensed ground stations in Brazil, a calibration field, and AI that turns images into answers for farms, forests and mines.',
  cta1='Contact us', cta2='See the chain',
  collar=[('216','satellites in the constellation design',''),('24','orbital planes',''),('6','licensed ground station sites in Brazil',''),('2028','first launch target','plan')],
  orbit_h='A constellation of optical and radar satellites',
  orbit_p='Optical satellites show field detail and crop health. Radar satellites image at night and through cloud, so the rainy season stops being a blind spot. The design and the paperwork are done; the build comes next.',
  orbit_cap=('Illustration','Constellation concept'),
  spec=[('Constellation','<span class="num">216</span> satellites in <span class="num">24</span> orbital planes',''),
        ('Each plane','<span class="num">7</span> optical + <span class="num">2</span> SAR radar satellites',''),
        ('Optical','<span class="num">0.5 m</span> panchromatic + near-infrared',''),
        ('Radar','Through cloud, day and night',''),
        ('Deployment','Two phases, Alya-1 and Alya-2, <span class="num">108</span> satellites each',''),
        ('ITU filing','Network ALYASPC, through Brazil’s ANATEL','Filed'),
        ('Frequency licence','ANATEL','Granted'),
        ('First launch','<span class="num">2028</span>','Target')],
  ground_h='A landing point in South America',
  ground_p='Six licensed ground station sites across Brazil. The first, in Tucano, Bahia, has its master plan and building design done, and the Bahia state government supports a control centre in the state technology park.',
  ground_cap=('Design render','Tucano ground station, Bahia'),
  bands=[('S band','Telemetry, tracking and command'),('X band','Image and payload downlink'),('6 sites','Licensed across Brazil'),('Tucano, Bahia','Master plan and building design complete')],
  strip=[('gs-front.jpg','Design render','Station building'),('gs-control.jpg','Design render','Control room'),('orbit-salvador.jpg','From orbit','Coastal city')],
  calib_h='A calibration field under clear skies',
  calib_p=['The calibration field sits at the Tucano site in Brazil’s semi-arid northeast, where there are few clouds all year and many usable satellite passes.',
           'Reflectance targets on the ground calibrate optical sensors; corner reflectors calibrate radar. The field serves our own satellites and can offer calibration to other operators.'],
  field_h='From image to answer',
  field_p='AgriEasy, built in Hong Kong, combines satellite images and weather data, runs them through AI, and sends small farmers crop alerts. Farmers use it free. Banks, insurers and exporters pay per hectare.',
  channels=[('WeChat','China'),('WhatsApp','Brazil'),('SMS','anywhere')],
  globe_alt='AgriEasy: from space to your farm. Satellite data feeds AI alerts on soil, water, climate, production and credit.',
  index=[('Agriculture','Emergence, field boundaries, crop health (NDVI), soil moisture, yield and harvest timing'),
         ('Forests and carbon','Tree counts, forest cover and health, EUDR deforestation checks, carbon monitoring'),
         ('Mining and geology','Ongoing mine monitoring, ground subsidence, geohazards before and after'),
         ('Disasters','Wildfire detection and source analysis, loss checks for insurance'),
         ('Oceans','Ship detection, coastline change, aquaculture rafts, red and green tides'),
         ('Cities and assets','Construction progress, oil storage estimates, airport activity, 3D city models')],
  proof_h='10 pilot projects delivered',
  proof_p='Each pilot ran the full workflow: collect the data, analyse it, write the report, deliver it, all on Chinese satellite data. We are now building that workflow into an automated platform.',
  cases=[('farmland.jpg','Coffee plantation','Compared images from four years ago with today to show no forest was cleared. The report meets the EU Deforestation Regulation and can go to lenders.','Export compliance'),
         ('orbit-dunes.jpg','Carbon credits','Counted and tracked native trees replanted by a low-income farming community. The report became the verification document carbon credit buyers accept.','Carbon markets'),
         ('mine.jpg','Mine monitoring','Monthly monitoring of a large mining site in Brazil, with data from several satellite operators, delivered on schedule.','Mining')],
  cases_note='Client names stay private under NDA. Images are representative.',
  pilot_k=('Sector','Data','Deliverable'),
  pilot_v=[('Export compliance','Optical, four years apart','EUDR deforestation report'),('Carbon markets','Optical, tree-by-tree counts','Verification report for credit buyers'),('Mining, Brazil','Optical from several operators','Monthly monitoring reports')],
  calib_svg=('Optical reflectance targets','SAR corner reflectors','Satellite pass','Schematic · not to scale'),
  stages=('Orbit → ground','Ground → calibration','Calibration → field'),
  sheet=[('orbit-pivots.jpg','Scene A','Centre pivots'),('orbit-dam.jpg','Scene B','Dam and reservoir'),('orbit-dunes.jpg','Scene C','Dunes and lagoon'),('orbit-fields.jpg','Scene D','Field mosaic')],
  tl_h='Seven years of groundwork',
  tl=[('2019','Alya Space founded in Brazil','Wins the Brazilian Air Force Amazonia 4.0 challenge','Done',''),
      ('2020','Two years with the Brazilian Air Force','Residency at IEAv / DCTA to validate the work','Done',''),
      ('2022','Paper at IAC Paris','International Astronautical Congress','Done',''),
      ('2023–24','Constellation designed and filed','Jianguo Chai and Ruoyu Li join; Alya Nanosatellites opens in Paris; ITU filing through ANATEL; G20 Space speaker','Done',''),
      ('2025','Jade Aerospace founded in Hong Kong','Selected for the Microsoft × HKSTP Co-Ideation programme','Done',''),
      ('2026','10 pilot projects delivered','Mining, coffee, carbon and land projects in Brazil and Africa; InnoCarnival 2026 space zone, Hong Kong','Done','now'),
      ('2027','Partners for satellites, stations and calibration','Build the first satellites and the Tucano ground station with partners','Planned','plan'),
      ('2027','AgriEasy first version','Satellite data, AI analysis and alerts, with the first trial users','Planned','plan'),
      ('2027','First paying customer','An insurer or bank, paying per hectare','Planned','plan'),
      ('2028','First satellite launch','Target for the first satellites of the constellation','Target','plan')],
  team_h='The team',
  team_p='Aila, Jianguo and Ruoyu have delivered every pilot together since 2023. Rhea is turning that workflow into the AI platform.',
  team=[('aila','Aila Raquel','Founder & CEO','Founder of Alya Space, Alya Nanosatellites and Jade Aerospace. Designed the constellation. Winner of the Brazilian Air Force Amazonia 4.0 challenge.'),
        ('chai','Jianguo Chai','CTO, Satellite & Ground Systems','Led ground station builds for more than 20 satellite projects, including Nigeria, Venezuela, Pakistan and Algeria.'),
        ('rhea','Rhea Lau','CTO, GeoAI','Geophysics and machine learning. ML research at SLB, then Arup and Fugro in Hong Kong. Leads the AI platform.'),
        ('li','Ruoyu Li','COO, Remote Sensing & Data Fusion','Remote sensing engineer. MSc in Applied GIS from the National University of Singapore. Multi-source satellite and drone data.')],
  hk_alt='Jade at the HKSTP space exhibit, InnoCarnival 2026, Hong Kong', hk_cap=('Hong Kong','InnoCarnival 2026 space zone'),
  crew=[('event-1.jpg','Team at a space industry event'),('event-2.jpg','Team at the Alya Space stand'),('event-3.jpg','Group photo with partners')],
  marks=['Microsoft × HKSTP Co-Ideation','Brazilian Air Force IEAv / DCTA','Amazonia 4.0 challenge winner','Bahia state government','IAC Paris 2022','G20 Space 2024'],
  c_h='Build the chain with us',
  c_p='We are talking to satellite makers and launch providers, ground station and calibration partners, satellite data suppliers, and banks, insurers and agribusiness who want answers from orbit.',
  copy='Copy email', f_name='Name', f_email='Email', f_org='Organisation', f_msg='Message', f_send='Send message',
  foot='© 2026 Jade Aerospace Limited 玉航天有限公司 · Hong Kong',
  fonts='family=Geist+Mono:wght@400;500&family=Manrope:wght@400;500;600&family=Space+Grotesk:wght@400;500&display=swap',
),
'zh': dict(
  lang='zh-Hans', p='../', other='../', otherlabel='EN', otherhreflang='en',
  title='玉航天 Jade Aerospace | 卫星星座、地面站与 AI 遥感分析',
  desc='玉航天是一家香港公司，建设完整的对地观测链条：216 颗卫星星座、巴西已获许可的地面站、定标场，以及 AI 遥感分析。',
  ogdesc='卫星、地面站与 AI：从轨道到田间。',
  skip='跳到正文', themeLabel='切换浅色 / 深色',
  nav=[('orbit','卫星星座'),('ground','地面站'),('field','农易'),('proof','项目'),('team','团队')],
  contact='联系我们',
  rail=[('orbit','轨道'),('ground','地面站'),('calibration','定标场'),('field','田间'),('proof','项目'),('timeline','历程'),('team','团队'),('contact','联系')],
  railLabel='页面导航',
  sceneL='玉航天 · 对地观测', sceneR='光学影像 · 灌溉农田',
  h1='从轨道<br>到田间。',
  lede='玉航天正在建设完整的对地观测链条：216 颗卫星星座、巴西已获许可的地面站、定标场，以及把影像变成结论的 AI，服务农业、林业和矿业。',
  cta1='联系我们', cta2='了解整条链',
  collar=[('216','颗卫星，星座设计',''),('24','个轨道面',''),('6','个巴西已获许可的地面站站址',''),('2028','首次发射目标','plan')],
  orbit_h='光学与雷达卫星组成的星座',
  orbit_p='光学卫星看清地块细节和作物长势；雷达卫星昼夜成像、穿透云层，雨季也不再是盲区。设计和申报已经完成，下一步是研制。',
  orbit_cap=('示意图','星座概念'),
  spec=[('星座','<span class="num">216</span> 颗卫星，<span class="num">24</span> 个轨道面',''),
        ('每个轨道面','<span class="num">7</span> 颗光学 + <span class="num">2</span> 颗 SAR 雷达卫星',''),
        ('光学','<span class="num">0.5 米</span>全色 + 近红外',''),
        ('雷达','穿透云层，昼夜成像',''),
        ('部署','分两期：Alya-1 与 Alya-2，各 <span class="num">108</span> 颗',''),
        ('ITU 申报','网络代号 ALYASPC，经巴西 ANATEL 提交','已提交'),
        ('频率许可','ANATEL','已获批'),
        ('首次发射','<span class="num">2028</span> 年','目标')],
  ground_h='南美的数据落脚点',
  ground_p='巴西 6 个已获许可的地面站站址。首站位于巴伊亚州图卡诺，已完成总体规划和建筑方案；巴伊亚州政府支持在州科技园设立控制中心。',
  ground_cap=('设计效果图','图卡诺地面站，巴伊亚州'),
  bands=[('S 频段','测控（TT&amp;C）'),('X 频段','影像与载荷数据下传'),('6 个站址','巴西境内已获许可'),('图卡诺','总体规划与建筑方案已完成')],
  strip=[('gs-front.jpg','设计效果图','站房'),('gs-control.jpg','设计效果图','控制室'),('orbit-salvador.jpg','卫星视角','沿海城市')],
  calib_h='晴空下的定标场',
  calib_p=['定标场位于巴西东北部半干旱区的图卡诺站址，全年云量少，可安排的过境观测次数多。',
           '光学传感器用地面反射靶标定标，SAR 雷达用角反射器定标。定标场服务我们自己的卫星，也可以为其他运营商提供定标服务。'],
  field_h='从影像到结论',
  field_p='AgriEasy 农易在香港研发：把卫星影像和气象数据交给 AI 分析，再给中小农户推送作物提示。农户免费使用，银行、保险公司和出口商按面积付费。',
  channels=[('微信','中国'),('WhatsApp','巴西'),('短信','通用')],
  globe_alt='AgriEasy 农易：从太空到你的农场，卫星数据经 AI 分析，提示土壤、水、气候、生产与信贷。',
  index=[('农业','出苗率、种植边界、长势（NDVI）、土壤湿度、产量与成熟期'),
         ('林业与碳汇','树木计数、森林覆盖与健康、EUDR 毁林核查、碳汇监测'),
         ('矿业与地质','矿区持续监测、地面沉降、地质灾害前后对比'),
         ('灾害','山火识别与火源分析、保险灾后损失核查'),
         ('海洋','船只检测、海岸线变化、养殖浮筏、赤潮绿潮'),
         ('城市与资产','施工进度、原油储量估算、机场动态、城市三维重建')],
  proof_h='10 个试点项目已交付',
  proof_p='每个试点都走完了完整流程：采集数据、分析、编写报告、交付，全部使用中国卫星数据。现在我们正把这套流程开发成自动化平台。',
  cases=[('farmland.jpg','咖啡种植园','对比 4 年前与当前影像，证明没有毁林。报告符合欧盟毁林法规（EUDR），也可提交给贷款方。','出口合规'),
         ('orbit-dunes.jpg','碳信用','对低收入农业社区补种的原生树进行卫星计数与监测，报告成为碳信用买家认可的核查文件。','碳市场'),
         ('mine.jpg','矿区监测','为巴西一个大型矿区按月持续监测，协调多家卫星运营商的数据，按时交付。','矿业')],
  cases_note='客户名称受保密协议约束，不予公开。图片仅作示意。',
  pilot_k=('行业','数据','交付'),
  pilot_v=[('出口合规','光学影像，相隔四年','EUDR 毁林核查报告'),('碳市场','光学影像，逐棵计数','供碳信用买家使用的核查报告'),('矿业，巴西','多家运营商的光学数据','每月监测报告')],
  calib_svg=('光学反射靶标','SAR 角反射器','卫星过境','示意图 · 非按比例'),
  stages=('轨道 → 地面站','地面站 → 定标场','定标场 → 田间'),
  sheet=[('orbit-pivots.jpg','影像 A','中心支轴喷灌'),('orbit-dam.jpg','影像 B','水坝与水库'),('orbit-dunes.jpg','影像 C','沙丘与潟湖'),('orbit-fields.jpg','影像 D','农田拼块')],
  tl_h='七年的前期积累',
  tl=[('2019','Alya Space 在巴西成立','获巴西空军 Amazonia 4.0 挑战赛冠军','已完成',''),
      ('2020','与巴西空军合作两年','在 IEAv / DCTA 驻所验证','已完成',''),
      ('2022','巴黎国际宇航大会发表论文','International Astronautical Congress (IAC)','已完成',''),
      ('2023–24','星座完成设计并申报','Jianguo Chai、Ruoyu Li 加入；Alya Nanosatellites 在巴黎成立；经 ANATEL 向 ITU 申报；G20 航天会议演讲','已完成',''),
      ('2025','玉航天在香港成立','入选 Microsoft × HKSTP 共创计划','已完成',''),
      ('2026','10 个试点项目交付','巴西和非洲的矿业、咖啡、碳汇与土地项目；InnoCarnival 2026 香港太空展区','已完成','now'),
      ('2027','卫星、地面站与定标场合作伙伴','与合作伙伴一起推进首批卫星和图卡诺地面站','计划中','plan'),
      ('2027','农易最小可用版本','卫星数据、AI 分析与提示推送，首批试用用户','计划中','plan'),
      ('2027','首个付费客户','保险公司或银行，按面积付费','计划中','plan'),
      ('2028','首次卫星发射','星座首批卫星的发射目标','目标','plan')],
  team_h='团队',
  team_p='Aila、Jianguo Chai 和 Ruoyu Li 自 2023 年起一起交付了全部试点项目；Rhea 负责把这套流程做成 AI 平台。',
  team=[('aila','Aila Raquel','创始人兼 CEO','Alya Space、Alya Nanosatellites 与玉航天创始人，负责星座设计；巴西空军 Amazonia 4.0 挑战赛冠军。'),
        ('chai','Jianguo Chai','CTO · 卫星与地面系统','主持尼日利亚、委内瑞拉、巴基斯坦、阿尔及利亚等 20 多个卫星项目的地面站建设。'),
        ('rhea','Rhea Lau','CTO · GeoAI','地球物理与机器学习背景；斯伦贝谢（SLB）机器学习研究，奥雅纳（Arup）、辉固（Fugro）香港。负责 AI 平台研发。'),
        ('li','Ruoyu Li','COO · 遥感与数据融合','遥感工程师，新加坡国立大学应用地理信息系统硕士；多源卫星与无人机数据处理。')],
  hk_alt='玉航天在 InnoCarnival 2026 香港太空展区', hk_cap=('香港','InnoCarnival 2026 太空展区'),
  crew=[('event-1.jpg','团队参加航天行业活动'),('event-2.jpg','团队在 Alya Space 展位'),('event-3.jpg','与合作伙伴合影')],
  marks=['Microsoft × HKSTP 共创计划','巴西空军 IEAv / DCTA','Amazonia 4.0 挑战赛冠军','巴伊亚州政府','2022 巴黎国际宇航大会','2024 G20 航天会议'],
  c_h='一起把这条链建起来',
  c_p='我们正在与卫星制造商和发射服务商、地面站与定标场伙伴、卫星数据供应商，以及希望从卫星数据中获得答案的银行、保险公司和农业企业洽谈合作。',
  copy='复制邮箱', f_name='姓名', f_email='邮箱', f_org='机构', f_msg='留言', f_send='发送',
  foot='© 2026 玉航天有限公司 Jade Aerospace Limited · 香港',
  fonts='family=Geist+Mono:wght@400;500&family=Manrope:wght@400;500;600&family=Noto+Sans+SC:wght@400;500&family=Space+Grotesk:wght@400;500&display=swap',
)}

def page(L):
    d=T[L]; p=d['p']; A=p+'assets/'
    nav=''.join(f'<a href="#{i}">{t}</a>' for i,t in d['nav'])
    rail=''.join(f'<li><a href="#{i}">{t}</a></li>' for i,t in d['rail'])
    collar=''.join(f'<div class="{c}"><b>{n}</b><span>{t}</span></div>' for n,t,c in d['collar'])
    def tag(s):
        if not s: return ''
        cls=' plan' if s in ('Target','目标') else ''
        return f'<span class="tag{cls}">{s}</span>'
    spec=''.join(f'<tr><th scope="row">{k}</th><td>{v}{tag(s)}</td></tr>' for k,v,s in d['spec'])
    bands=''.join(f'<div><b>{a}</b><span>{b}</span></div>' for a,b in d['bands'])
    strip=''.join(f'<figure><div class="frame"><img src="{A}{f}" alt="{c2}" loading="lazy"></div><figcaption class="cap"><span>{c1}</span><b>{c2}</b></figcaption></figure>' for f,c1,c2 in d['strip'])
    calib=''.join(f'<p>{x}</p>' for x in d['calib_p'])
    ch=''.join(f'<span><b>{a}</b> · {b}</span>' for a,b in d['channels'])
    idx=''.join(f'<li><b>{a}</b><span>{b}</span></li>' for a,b in d['index'])
    K=d['pilot_k']
    cases=''.join(f'<article class="pilot"><div class="frame"><img src="{A}{f}" alt="" loading="lazy"></div><div class="txt"><h3>{h}</h3><p>{t}</p><table class="spec"><tbody><tr><th scope="row">{K[0]}</th><td>{v[0]}</td></tr><tr><th scope="row">{K[1]}</th><td>{v[1]}</td></tr><tr><th scope="row">{K[2]}</th><td>{v[2]}</td></tr></tbody></table></div></article>' for (f,h,t,u),v in zip(d['cases'],d['pilot_v']))
    sb=lambda lab: '<div class="scalebar" aria-hidden="true"><i></i><i></i><i></i><i></i></div>'
    c=d['calib_svg']
    calsvg=f'''<figure class="calib-plate frame"><svg viewBox="0 0 1200 420" role="img" aria-label="{c[3]}">
<defs><pattern id="g" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#1E3A40" stroke-width="1"/></pattern></defs>
<rect width="1200" height="420" fill="url(#g)"/>
<path d="M60 196 L1140 36" stroke="#51BAC1" stroke-width="1.5" stroke-dasharray="6 8" fill="none"/>
<text class="lbl" x="980" y="96" fill="#51BAC1" font-family="Space Grotesk, Noto Sans SC, sans-serif" font-size="15" letter-spacing="1">{c[2]}</text>
<g transform="translate(160 220)">
<rect x="0" y="0" width="70" height="70" fill="#F2F5F4"/><rect x="80" y="0" width="70" height="70" fill="#B9CBC9"/><rect x="160" y="0" width="70" height="70" fill="#7F9A98"/><rect x="240" y="0" width="70" height="70" fill="#2C5158"/>
<path d="M0 100 H310" stroke="#51BAC1" stroke-width="1"/><path d="M0 95 v10 M310 95 v10" stroke="#51BAC1" stroke-width="1"/>
<text class="lbl" x="0" y="132" fill="#B9CBC9" font-family="Space Grotesk, Noto Sans SC, sans-serif" font-size="16">{c[0]}</text></g>
<g transform="translate(700 230)" fill="none" stroke="#F2F5F4" stroke-width="1.5">
<path d="M0 60 L30 0 L60 60 Z"/><path d="M110 60 L140 0 L170 60 Z"/><path d="M220 60 L250 0 L280 60 Z"/>
<path d="M30 0 V60 M140 0 V60 M250 0 V60" stroke="#51BAC1" stroke-width="1"/>
<path d="M0 90 H280" stroke="#51BAC1" stroke-width="1"/><path d="M0 85 v10 M280 85 v10" stroke="#51BAC1" stroke-width="1"/>
<text class="lbl" x="0" y="122" fill="#B9CBC9" stroke="none" font-family="Space Grotesk, Noto Sans SC, sans-serif" font-size="16">{c[1]}</text></g>
<text class="lbl" x="28" y="44" fill="#7F9A98" font-family="Space Grotesk, Noto Sans SC, sans-serif" font-size="13" letter-spacing="1.5">{c[3].upper()}</text>
</svg><figcaption class="calib-legend"><span><i class="sw t"></i>{c[0]}</span><span><i class="sw r"></i>{c[1]}</span><span><i class="sw p"></i>{c[2]}</span><span>{c[3]}</span></figcaption></figure>'''
    sheet=''.join(f'<figure class="frame"><img src="{A}{f}" alt="{b}" loading="lazy"><figcaption><span>{a}</span><span>{b}</span></figcaption></figure>' for f,a,b in d['sheet'])
    tl=''.join(f'<li class="{c}"><span class="yr">{y}</span><b>{h}</b><span>{t}</span><span class="st">{s}</span></li>' for y,h,t,s,c in d['tl'])
    team=''.join(f'<article class="person"><img src="{A}team-{k}.jpg" alt="{n}" loading="lazy"><h3>{n}</h3><p class="role">{r}</p><p>{b}</p></article>' for k,n,r,b in d['team'])
    crew=''.join(f'<figure><div class="frame"><img src="{A}{f}" alt="{a}" loading="lazy"></div></figure>' for f,a in d['crew'])
    marks=''.join(f'<span>{m}</span>' for m in d['marks'])
    return f'''<!doctype html>
<html lang="{d['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{d['title']}</title>
<meta name="description" content="{d['desc']}">
<meta name="theme-color" content="#061418" media="(prefers-color-scheme: dark)">
<meta name="theme-color" content="#F4F7F6" media="(prefers-color-scheme: light)">
<script>try{{var t=localStorage.getItem("theme");if(t==="light"||t==="dark")document.documentElement.dataset.theme=t}}catch(e){{}}</script>
<meta property="og:title" content="Jade Aerospace">
<meta property="og:description" content="{d['ogdesc']}">
<meta property="og:image" content="https://jadeaerospace.com/assets/hero-fields.jpg">
<link rel="alternate" hreflang="en" href="https://jadeaerospace.com/">
<link rel="alternate" hreflang="zh-Hans" href="https://jadeaerospace.com/zh/">
<link rel="icon" href="{A}logo-jade.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?{d['fonts']}" rel="stylesheet">
<link rel="stylesheet" href="{A}style.css">
<script src="{A}site.js" defer></script>
</head>
<body>
<a class="skip" href="#orbit">{d['skip']}</a>

<!-- ============ TOP BAR ============ -->
<header class="top">
  <div class="wrap">
    <a class="logo" href="./"><img class="on-dark" src="{A}logo-white.png" alt="Jade Aerospace"><img class="on-light" src="{A}logo-jade.png" alt="Jade Aerospace"></a>
    <nav>
      {nav}
      <button type="button" class="theme" data-theme-toggle aria-label="{d['themeLabel']}" title="{d['themeLabel']}"><svg class="moon" viewBox="0 0 16 16" aria-hidden="true"><path d="M13.5 10.2A6 6 0 0 1 5.8 2.5a6 6 0 1 0 7.7 7.7Z" fill="none" stroke="currentColor" stroke-width="1.3"/></svg><svg class="sun" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="3" fill="none" stroke="currentColor" stroke-width="1.3"/><path d="M8 1v2M8 13v2M1 8h2M13 8h2M3 3l1.4 1.4M11.6 11.6 13 13M3 13l1.4-1.4M11.6 4.4 13 3" stroke="currentColor" stroke-width="1.3"/></svg></button>
      <a class="lang" href="{d['other']}" hreflang="{d['otherhreflang']}">{d['otherlabel']}</a>
      <a class="cta-top" href="#contact">{d['contact']}</a>
    </nav>
  </div>
</header>

<!-- Stage rail: one link per section below. Keep ids in step. -->
<nav class="rail" aria-label="{d['railLabel']}"><ol>{rail}</ol></nav>

<main class="main">

<!-- ============ HERO ============ -->
<section class="hero">
  <div class="frame">
    <div class="bg"><img src="{A}hero-fields.jpg" alt="" fetchpriority="high"></div>
    <div class="scene-id"><span>{d['sceneL']}</span><span>{d['sceneR']}</span></div>
    <div class="copy">
      <h1>{d['h1']}</h1>
      <p class="lede">{d['lede']}</p>
      <div class="actions">
        <a class="btn" href="#contact">{d['cta1']} {ARROW}</a>
        <a class="btn ghost" href="#orbit">{d['cta2']} {DOWN}</a>
      </div>
    </div>
    <div class="collar">{collar}</div>
  </div>
</section>

<!-- ============ ORBIT: constellation ============ -->
<section class="sec orbit" id="orbit">
  <div class="wrap">
    <div class="sec-head"><h2>{d['orbit_h']}</h2><p>{d['orbit_p']}</p></div>
    <div class="grid12">
      <figure class="media" style="margin:0">
        <div class="frame"><img src="{A}constellation.jpg" alt="" loading="lazy"></div>
        <figcaption class="cap"><span>{d['orbit_cap'][0]}</span><b>{d['orbit_cap'][1]}</b></figcaption>
      </figure>
      <div class="side"><table class="spec"><tbody>{spec}</tbody></table></div>
    </div>
  </div>
</section>

<!-- ============ GROUND: stations ============ -->
<section class="sec" id="ground">
  <div class="wrap">{sb(d['stages'][0])}</div>
  <figure class="bleed" style="margin-top:0;margin-bottom:0">
    <div class="frame"><img src="{A}gs-tucano.jpg" alt="{d['ground_cap'][1]}" loading="lazy"></div>
    <div class="over"><h2>{d['ground_h']}</h2><p>{d['ground_p']}</p></div>
  </figure>
  <div class="wrap">
    <p class="cap"><span>{d['ground_cap'][0]}</span><b>{d['ground_cap'][1]}</b></p>
    <div class="bands">{bands}</div>
    <div class="strip">{strip}</div>
  </div>
</section>

<!-- ============ CALIBRATION ============ -->
<section class="sec" id="calibration">
  <div class="wrap">
    {sb(d['stages'][1])}
    <div class="calib">
      <h2>{d['calib_h']}</h2>
      <div class="body">{calib}</div>
      {calsvg}
    </div>
  </div>
</section>

<!-- ============ FIELD: AgriEasy ============ -->
<section class="sec field" id="field">
  <div class="wrap">{sb(d['stages'][2])}</div>
  <div class="wrap grid12">
    <div class="globe"><img src="{A}agrieasy-globe.jpg" alt="{d['globe_alt']}" loading="lazy"></div>
    <div class="side">
      <h2>{d['field_h']}</h2>
      <p style="color:var(--ink-2);margin-top:22px">{d['field_p']}</p>
      <div class="channels">{ch}</div>
      <ul class="index">{idx}</ul>
    </div>
  </div>
</section>

<!-- ============ PROOF: pilots ============ -->
<section class="sec" id="proof">
  <div class="wrap">
    <div class="sec-head"><h2>{d['proof_h']}</h2><p>{d['proof_p']}</p></div>
    <div class="pilots">{cases}</div>
    <p class="note">{d['cases_note']}</p>
    <div class="contact-sheet">{sheet}</div>
  </div>
</section>

<!-- ============ TIMELINE ============ -->
<section class="sec" id="timeline">
  <div class="wrap">
    <div class="sec-head"><h2>{d['tl_h']}</h2></div>
    <ol class="ledger">{tl}</ol>
  </div>
</section>

<!-- ============ TEAM ============ -->
<section class="sec" id="team">
  <div class="wrap">
    <div class="sec-head"><h2>{d['team_h']}</h2><p>{d['team_p']}</p></div>
    <div class="team">{team}</div>
    <figure class="wide-photo" style="margin:0">
      <div class="frame"><img src="{A}event-hk.jpg" alt="{d['hk_alt']}" loading="lazy"></div>
      <figcaption class="cap"><span>{d['hk_cap'][0]}</span><b>{d['hk_cap'][1]}</b></figcaption>
    </figure>
    <div class="crew">{crew}</div>
    <div class="marks">{marks}</div>
  </div>
</section>

<!-- ============ CONTACT ============ -->
<section class="contact" id="contact">
  <div class="wrap grid12">
    <div class="left">
      <h2>{d['c_h']}</h2>
      <p>{d['c_p']}</p>
      <div class="mailrow"><code>aila@alyaspace.com</code><button type="button" data-copy>{d['copy']}</button></div>
    </div>
    <form id="contact-form" class="cform">
      <div class="row">
        <label>{d['f_name']}<input name="name" required autocomplete="name"></label>
        <label>{d['f_email']}<input name="email" type="email" required autocomplete="email"></label>
      </div>
      <label>{d['f_org']}<input name="org" autocomplete="organization"></label>
      <label>{d['f_msg']}<textarea name="message" required></textarea></label>
      <input class="hp" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
      <button type="submit" class="btn">{d['f_send']} {ARROW}</button>
      <p class="form-msg" role="status"></p>
    </form>
  </div>
</section>

</main>

<footer>
  <div class="wrap">
    <span>{d['foot']}</span>
    <a href="mailto:aila@alyaspace.com">aila@alyaspace.com</a>
  </div>
</footer>

<script src="{A}contact.js" defer></script>
</body>
</html>
'''
open(root+'/index.html','w').write(page('en'))
open(root+'/zh/index.html','w').write(page('zh'))
print('built')

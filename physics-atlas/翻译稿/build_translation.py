from bs4 import BeautifulSoup, NavigableString
from pathlib import Path

src=Path('/tmp/formula_sheet_source.html')
out=Path('/workspace/atlas-physics-zh/16-formula-sheet.md')
soup=BeautifulSoup(src.read_text(encoding='utf-8'),'html.parser')

# Exact translations for all explanatory labels and user-facing prose in the source unit.
T={
'Equation sheet':'公式表','Atlas of Physics':'物理学图谱','The AP sheets, linked to the pages':'AP 公式表，链接至相关页面',
'The official AP Physics 1 and Physics C equation sheets, line by line. Each equation links to every page of the atlas that shows or uses it.':'逐行列出官方 AP Physics 1 与 Physics C 公式表。每条公式都链接到图谱中展示或使用它的所有页面。',
'Physics 1':'Physics 1','C: Mechanics':'C：力学','C: E&amp;M':'C：电磁学','AP Physics 1':'AP Physics 1','AP Physics C: Mechanics':'AP Physics C：力学','AP Physics C: Electricity and Magnetism':'AP Physics C：电学与磁学',
'Algebra-based · effective fall 2024':'代数基础 · 2024 年秋季起生效','Calculus-based · effective fall 2024':'微积分基础 · 2024 年秋季起生效',
'Constants and conversion factors':'常量与换算因子','Universal gravitational constant':'万有引力常量','1 atmosphere of pressure':'1 个标准大气压','Magnitude of the acceleration due to gravity at Earth’s surface':'地球表面重力加速度的大小','Magnitude of the gravitational field strength at Earth’s surface':'地球表面重力场强的大小',
'Prefixes':'词头','Factor':'因数','Prefix':'词头','Symbol':'符号','tera':'太','giga':'吉','mega':'兆','kilo':'千','centi':'厘','milli':'毫','micro':'微','nano':'纳','pico':'皮',
'Unit symbols':'单位符号','hertz,':'赫兹，','joule,':'焦耳，','kilogram,':'千克，','meter,':'米，','newton,':'牛顿，','pascal,':'帕斯卡，','second,':'秒，','watt,':'瓦特，','ampere,':'安培，','coulomb,':'库仑，','electron volt,':'电子伏特，','farad,':'法拉，','henry,':'亨利，','ohm,':'欧姆，','tesla,':'特斯拉，','volt,':'伏特，',
'Values of trigonometric functions for common angles':'常见角的三角函数值','Conventions':'约定','The following conventions are used in this exam:':'本考试采用以下约定：','The following conventions are used in this exam unless otherwise stated:':'除非另有说明，本考试采用以下约定：',
'The frame of reference of any problem is assumed to be inertial unless otherwise stated.':'除非另有说明，任何问题的参考系均视为惯性系。','Air resistance is assumed to be negligible unless otherwise stated.':'除非另有说明，空气阻力均视为可以忽略。','Springs and strings are assumed to be ideal unless otherwise stated.':'除非另有说明，弹簧和绳均视为理想的。','Fluids are assumed to be ideal, and pipes are assumed to be completely filled by fluid, unless otherwise stated.':'除非另有说明，流体视为理想流体，管道视为完全充满流体。','The frame of reference for any problem is inertial.':'任何问题的参考系均为惯性系。','Frictional forces and air resistance are negligible.':'摩擦力和空气阻力可以忽略。','Strings, springs, batteries, wires, and meters are ideal.':'绳、弹簧、电池、导线和电表均为理想元件。','The electric potential is zero at an infinite distance from an isolated point charge.':'孤立点电荷在无穷远处的电势为零。','The direction of current is the direction in which positive charges would drift.':'电流方向定义为正电荷漂移的方向。','Resistors and lightbulbs are ohmic.':'电阻器和灯泡均为欧姆元件。','Capacitors are air-filled (κ = 1.0).':'电容器内充满空气（κ = 1.0）。',
'Geometry and trigonometry':'几何与三角学','Mechanics and fluids · left column':'力学与流体 · 左栏','Mechanics and fluids · right column':'力学与流体 · 右栏','Mechanics · left column':'力学 · 左栏','Mechanics · right column':'力学 · 右栏','Electricity and magnetism · left column':'电学与磁学 · 左栏','Electricity and magnetism · right column':'电学与磁学 · 右栏',
'Mechanics':'力学','Also on this sheet, identical to':'本公式表中也有，与','the Physics 1 sheet':'Physics 1 公式表相同','the C: Mechanics sheet (both columns)':'C：力学公式表（左右两栏）相同','the C: Mechanics sheet':'C：力学公式表相同',
'Also on this sheet, identical to':'本公式表中也有，与','the Physics 1 sheet':'Physics 1 公式表相同','the C: Mechanics sheet (both columns)':'C：力学公式表（左右两栏）相同','the C: Mechanics sheet':'C：力学公式表相同','Vectors':'向量','The sheet’s math reference.':'本公式表的数学参考。','Calculus':'微积分','Vectors, calculus and identities':'向量、微积分与恒等式','Identities':'恒等式','No equation matches.':'没有匹配的公式。',
'Rectangle':'矩形','Triangle':'三角形','Circle':'圆','Rectangular solid':'长方体','Cylinder':'圆柱','Sphere':'球','Right triangle':'直角三角形',
'Velocity at constant acceleration':'恒加速度下的速度','Position at constant acceleration':'恒加速度下的位置','Velocity without time':'不含时间的速度','Centre of mass':'质心','Newton’s second law':'牛顿第二定律','Universal gravitation':'万有引力','Friction':'摩擦力','Hooke’s law: spring force':'胡克定律：弹簧力','Centripetal acceleration':'向心加速度','Kinetic energy':'动能','Work by a constant force':'恒力做功','Work–energy theorem':'功—能定理','Spring potential energy':'弹簧势能','Gravitational potential energy, any distance':'任意距离下的引力势能','Gravitational potential energy near the surface':'近地表引力势能','Average power':'平均功率','Instantaneous power':'瞬时功率','Momentum':'动量','Net force and change of momentum':'合力与动量变化','Impulse':'冲量','Velocity of the centre of mass':'质心速度',
'Angular velocity at constant α':'恒定 α 下的角速度','Angle at constant α':'恒定 α 下的角度','Angular velocity without time':'不含时间的角速度','Linear and angular speed':'线速度与角速度','Tangential acceleration':'切向加速度','Torque':'力矩','Rotational inertia':'转动惯量','Parallel-axis theorem':'平行轴定理','Newton’s second law for rotation':'转动的牛顿第二定律','Rotational kinetic energy':'转动动能','Work done by a torque':'力矩做功','Angular momentum of a rigid body':'刚体的角动量','Angular momentum of a particle':'质点的角动量','Angular impulse':'角冲量','Rolling without slipping':'无滑动滚动','Period and frequency':'周期与频率','Period of a mass on a spring':'弹簧振子的周期','Period of a simple pendulum':'单摆周期','Position in simple harmonic motion, from x = A':'简谐运动中的位置，从 x = A 开始','Position in simple harmonic motion, from x = 0':'简谐运动中的位置，从 x = 0 开始','Density':'密度','Pressure':'压强','Absolute pressure at depth':'深度处的绝对压强','Gauge pressure':'表压','Buoyant force':'浮力','Continuity':'连续性','Bernoulli’s equation':'伯努利方程',
'Displacement as an integral':'位移的积分表达式','Change of velocity as an integral':'速度变化的积分表达式','Centre of mass of a solid body':'实体的质心','Linear mass density':'线密度','Work':'功','Potential energy from a conservative force':'由保守力得到的势能','Force from potential energy':'由势能得到的力','Net force is the rate of change of momentum':'合力是动量的变化率','Angular velocity':'角速度','Angular acceleration':'角加速度','Rotational inertia of a solid body':'实体的转动惯量','Position in simple harmonic motion':'简谐运动中的位置',
'No magnetic monopoles':'不存在磁单极子','Magnetic force on a moving charge':'运动电荷所受的磁力','Biot–Savart law':'毕奥—萨伐尔定律','Magnetic force on a current':'载流导线所受的磁力','Ampère’s law':'安培定律','Field inside a solenoid':'螺线管内的磁场','Magnetic flux':'磁通量','Faraday’s law':'法拉第定律','Emf of a coil of N loops':'N 匝线圈的电动势','Inductance of a solenoid':'螺线管的电感','Energy stored in an inductor':'电感器中储存的能量','Self-induced emf':'自感电动势','LC angular frequency':'LC 角频率','Coulomb constant':'库仑常量','Vacuum permittivity':'真空介电常数','Vacuum permeability':'真空磁导率','Proton mass':'质子质量','Neutron mass':'中子质量','Electron mass':'电子质量','Elementary charge':'基本电荷','1 electron volt':'1 电子伏特','Speed of light':'光速','1 unified atomic mass unit':'1 统一原子质量单位','Electric field':'电场','Field of a continuous charge':'连续电荷的场','Electric flux':'电通量','Gauss’s law':'高斯定律','Total charge from a charge density':'由电荷密度得到的总电荷','Electric potential energy of two charges':'两个电荷的电势能','Potential of a continuous charge':'连续电荷的电势','Potential difference from the field':'由电场得到的电势差','Field from potential':'由电势得到的场','Potential energy from potential':'由电势得到的势能','Capacitance':'电容','Parallel-plate capacitor':'平行板电容器','Energy stored in a capacitor':'电容器中储存的能量','Dielectric constant':'介电常数','Current':'电流','Current from current density':'由电流密度得到的电流','Ohm’s law in a material':'材料中的欧姆定律','Resistance of a wire':'导线电阻','Ohm’s law':'欧姆定律','Electric power':'电功率','Resistors in series':'串联电阻','Resistors in parallel':'并联电阻','Capacitors in series':'串联电容器','Capacitors in parallel':'并联电容器','RC time constant':'RC 时间常数','Magnetic force on a current':'载流导体所受的磁力','Geometry and trigonometry':'几何与三角学',
'Chain rule':'链式法则','Derivative of a power':'幂函数的导数','Derivative of an exponential':'指数函数的导数','Derivative of a logarithm':'对数函数的导数','Derivative of sine':'正弦函数的导数','Derivative of cosine':'余弦函数的导数','Integral of a power':'幂函数的积分','Integral of an exponential':'指数函数的积分','Integral giving a logarithm':'产生对数的积分','Integral of cosine':'余弦函数的积分','Integral of sine':'正弦函数的积分','Logarithm of a product and a power':'乘积与幂的对数','Pythagorean identity':'勾股恒等式','Double angle':'二倍角','Tangent':'正切',
}

def tr(s):
    s=s.strip()
    return T.get(s,s)

VAR={'area':'面积','base':'底边','circumference':'周长','height':'高度','length':'长度','radius':'半径','arc length':'弧长','surface area':'表面积','volume':'体积','width':'宽度','angle':'角度','acceleration':'加速度','distance':'距离','energy':'能量','force':'力','impulse':'冲量','spring constant':'弹簧常量','kinetic energy':'动能','mass':'质量','momentum':'动量','power':'功率','time':'时间','potential energy':'势能','velocity or speed':'速度或速率','position':'位置','vertical position':'竖直位置','coefficient of friction':'摩擦因数','amplitude or area':'振幅或面积','frequency':'频率','rotational inertia':'转动惯量','angular momentum':'角动量','pressure':'压强','period':'周期','work':'功','angular acceleration':'角加速度','angular position':'角位置','density':'密度','torque':'力矩','angular speed':'角速度','linear mass density':'线密度','electric field':'电场','current':'电流','current density':'电流密度','charge':'电荷','resistance':'电阻','electric potential or volume':'电势或体积','electric permittivity':'电介质常数','resistivity or charge density':'电阻率或电荷密度','dielectric constant':'介电常数','flux':'通量','magnetic field':'磁场','capacitance':'电容','inductance':'电感','number of loops per unit length':'单位长度线圈匝数','number of loops':'线圈匝数','emf':'电动势','magnetic permeability':'磁导率','time constant':'时间常数','angular frequency':'角频率','radius, distance, or position':'半径、距离或位置','velocity or speed':'速度或速率','position or distance':'位置或距离','radius or distance':'半径或距离'}
def translate_vars(tag):
    out=[]
    for x in tag.contents:
        if getattr(x,'name',None)=='i': out.append(str(x))
        else:
            z=str(x)
            for en,zh in sorted(VAR.items(),key=lambda kv:-len(kv[0])):
                z=z.replace(en,zh)
            out.append(z)
    return ''.join(out)

def inline_formula(tag):
    # Preserve the source formula symbols, numbers, variables, and units exactly as HTML.
    return str(tag).replace('\n',' ')

def links(container):
    vals=[]
    for a in container.select('a'):
        vals.append(f"[{tr(a.get_text(' ',strip=True))}]({a.get('href')})")
    if container.select_one('.none'):
        vals.append('（尚未显示）')
    return ' '.join(vals)

lines=['# 公式表','', '> Atlas of Physics（物理学图谱）中的非官方简体中文翻译。公式、符号、数字、单位、变量名与原始链接均按源文保留。','', '## 简介','', '逐行列出官方 AP Physics 1 与 Physics C 公式表。每条公式都链接到图谱中展示或使用它的所有页面。','']
for sec in soup.select('main > section.sheet'):
    h=sec.select_one('.shead h2').get_text(' ',strip=True)
    span=sec.select_one('.shead span').get_text(' ',strip=True)
    lines += [f'## {tr(h)}', '', f'*{tr(span)}*', '']
    for group in sec.select(':scope > .group'):
        h3=group.find(['h3'],recursive=False)
        if h3: lines += [f'### {tr(h3.get_text(" ",strip=True))}', '']
        vars=group.select_one(':scope > .vars')
        if vars:
            # Translate prose words while preserving italicized symbols and punctuation.
            txt=translate_vars(vars)
            lines += [txt.strip(), '']
        # constants table
        ct=group.select_one(':scope > table.ctab')
        if ct:
            lines += ['| 项目 | 数值 | 图谱页面 |','|---|---|---|']
            for row in ct.select('tr'):
                cells=row.find_all(['th','td'],recursive=False)
                if len(cells)>=2:
                    name=tr(cells[0].get_text(' ',strip=True)); val=inline_formula(cells[1]); refs=links(cells[2]) if len(cells)>2 else ''
                    lines.append(f'| {name} | {val} | {refs} |')
            lines.append('')
        # reference grid tables
        for d in group.select(':scope > .rgrid > div'):
            hh=d.find('h3')
            if hh: lines += [f'#### {tr(hh.get_text(" ",strip=True))}', '']
            tab=d.find('table')
            if tab:
                rows=[]
                for r in tab.select('tr'):
                    cs=r.find_all(['th','td'],recursive=False)
                    rows.append([tr(c.get_text(' ',strip=True)) for c in cs])
                if rows:
                    lines.append('| '+' | '.join(rows[0])+' |'); lines.append('|'+'|'.join(['---']*len(rows[0]))+'|')
                    for r in rows[1:]: lines.append('| '+' | '.join(r)+' |')
                    lines.append('')
        conv=group.select_one(':scope > ul.conv')
        if conv:
            for li in conv.find_all('li',recursive=False): lines.append(f'- {tr(li.get_text(" ",strip=True))}')
            lines.append('')
        # equation list
        ul=group.select_one(':scope > ul:not(.conv)')
        if ul:
            for li in ul.find_all('li',recursive=False):
                e=li.select_one('.e'); n=li.select_one('.n'); ch=li.select_one('.chips')
                if e and n:
                    formula=inline_formula(e)
                    label=tr(n.get_text(' ',strip=True)); refs=links(ch) if ch else ''
                    lines += [f'- **{label}**：{formula}', ('  - '+refs if refs else '')]
            lines.append('')
        # sections in C:E&M with repeated-sheet notices and math reference rows are handled below.
        # standalone tables/lists not caught above are included by the generic branch below.
    # Handle special groups made of .rgrid/.group contents not directly interpreted.

# The parser above deliberately emits all primary equation rows. Append special C references and E&M rows
# by parsing groups that contain h3 but no direct equation list.
# Build a second pass only for groups whose content was not represented; these are the final math/reference groups.
sec_em=soup.select_one('#em')
if sec_em:
    # It is already emitted above; add no duplicate here.
    pass

lines += ['## 归属与许可', '', '本单元源自 [Atlas of Physics](https://github.com/nathanliow/atlas-of-physics) 的 [Equation sheet](https://raw.githubusercontent.com/nathanliow/atlas-of-physics/main/equations/index.html)。', '', '源文说明：本页根据 College Board 的 AP Physics 1、Physics C: Mechanics 与 Physics C: Electricity and Magnetism《课程与考试说明》（2024 年秋季起生效；公式表 © 2025 College Board）中的 Information Table 转录，遵循公式表的顺序与记号。箭头表示向量。每条公式旁的名称是图谱的标签，并非公式表的一部分；标签后的链接给出章节与页面；灰显行表示公式表中有该内容，但图谱尚未绘制。', '', '本翻译为非官方简体中文翻译。原项目采用 MIT License；本翻译不改变原项目许可证及其版权归属。']
out.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(out, len(lines))

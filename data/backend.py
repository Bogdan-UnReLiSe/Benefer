heading_mark = '<!--Benefer: Website builder-->'
paragraph_mark = 'paragraph'
image_mark = 'img'
rect_mark = 'rect'
oval_mark = 'oval'
line_mark = 'line'
tab_mark = 'tab'
icon_mark = 'icon'
title_mark = 'title'
number_mark = 'number'
figure_bracket_open = '{'
figure_bracket_close = '}'


class Paragraph:
    def __init__(self, text, x, y, width, color, font, font_size, index, links, name, start_obj=None, rel=-1):
        self.main_code = []
        self.type = 'element'
        self.style = []
        self.rel = rel
        self.cipher = ''
        self.text = text
        self.text_code = text
        self.x = [x[0], x[1]]
        self.y = [y[0], y[1]]
        self.x_code = [x[0], x[1]]
        self.y_code = [y[0], y[1]]
        self.width = width
        self.width_code = width
        self.color = color
        self.font = font
        self.font_size = font_size
        self.index = index
        self.links = links
        self.name = name
        self.start_obj = start_obj

    def edit_text(self):
        self.text = self.text_code
        for link in self.links:
            symbols = []
            d = len(link[0])

            for i in range(0, len(self.text)-d+1):
                if self.text[i:i+d] == link[0]:
                    symbols.append(i)
            if len(symbols) == 2:
                self.text = self.text[0:symbols[0]] + f'<a href="{link[1]}">' + self.text[symbols[0]+d:symbols[1]] + \
                             '</a>' + self.text[symbols[1]+d:]

    def set_style(self):
        head = f'\t\t\t.c{self.index}' + ' {\n'
        close = '\t\t\t}\n'
        param = []
        param.append(f'\tposition:absolute;\n')
        if self.start_obj is not None:
            self.x[0] = f'calc({self.x_code[0]}{self.x_code[1]} + {self.start_obj.x[0]}{self.start_obj.x[1]})'
            self.x[1] = ''
            self.y[0] = f'calc({self.y_code[0]}{self.y_code[1]} + {self.start_obj.y[0]}{self.start_obj.y[1]})'
            self.y[1] = ''
        if self. width_code == ['', '']:
            self.width = [f'calc(100vw - {self.x[0]}{self.x[1]})', '']
        param.append(f'\tleft:{self.x[0]}{self.x[1]};\n')
        param.append(f'\ttop:{self.y[0]}{self.y[1]};\n')
        param.append('\ttext-align:justify;\n')
        if self.width != ('', ''):
            param.append(f'\twidth:{self.width[0]}{self.width[1]};\n')
        param.append(f'\tcolor:{self.color};\n')
        param.append(f'\tfont-family:{self.font};\n')
        param.append(f'\tfont-size:{self.font_size[0]}{self.font_size[1]};\n')

        for i in range(0, len(param)):
            param[i] = '\t\t\t' + param[i]

        self.style = [head] + param + [close]

    def cryptographer(self):
        self.cipher = f'{paragraph_mark}&' + \
                      f'{str(self.x_code[0])}^{self.x_code[1]}&' + \
                      f'{str(self.y_code[0])}^{self.y_code[1]}&' + \
            f'{self.width_code[0]}^{self.width_code[1]}' + \
            f'&{self.color}&{self.font}&{self.font_size[0]}^{self.font_size[1]}&{self.name}&{self.rel}'
        self.cipher = '\t\t<!--' + self.cipher + '-->\n' + '\t\t<!--' + self.text + '-->\n'
        links = ''
        for p in self.links:
            links += f'{p[0]}^{p[1]}&'
        self.cipher += '\t\t<!--' + links[:-1] + '-->\n'
        self.main_code = [self.cipher] + self.main_code

    def set_code(self):
        self.edit_text()
        self.main_code = [f'\t\t<div class="c{self.index}">\n', f'\t\t\t{self.text}\n', '\t\t</div>\n']
        self.cryptographer()


class Image:
    def __init__(self, src, x, y, width, height, index, alt, name, start_obj=None, rel=-1):
        self.type = 'element'
        self.rel = rel
        self.main_code = []
        self.style = []
        self.position = ''
        self.src = src
        self.x = [x[0], x[1]]
        self.y = [y[0], y[1]]
        self.x_code = [x[0], x[1]]
        self.y_code = [x[0], x[1]]
        self.width = width
        self.height = height
        self.index = index
        self.alt = alt
        self.cipher = ''
        self.name = name
        self.start_obj = start_obj

    def cryptographer(self):
        self.cipher = f'{image_mark} {self.src}&' + \
                      f'{str(self.x_code[0])}^{self.x_code[1]}&' + \
                      f'{str(self.y_code[0])}^{self.y_code[1]}&' + \
            f'{self.width[0]}^{self.width[1]}&{self.height[0]}^{self.height[1]}&{self.alt}&{self.name}&{self.rel}'
        self.cipher = '\t\t<!--' + self.cipher + '-->\n'
        self.main_code = [self.cipher] + self.main_code

    def set_style(self):
        head = f'\t\t\t.c{self.index}' + ' {\n'
        close = '\t\t\t}\n'
        param = []
        param.append(f'position:absolute;\n')
        if self.start_obj is not None:
            self.x[0] = f'calc({self.x_code[0]}{self.x_code[1]} + {self.start_obj.x[0]}{self.start_obj.x[1]})'
            self.x[1] = ''
            self.y[0] = f'calc({self.y_code[0]}{self.y_code[1]} + {self.start_obj.y[0]}{self.start_obj.y[1]})'
            self.y[1] = ''
        param.append(f'left:{self.x[0]}{self.x[1]};\n')
        param.append(f'top:{self.y[0]}{self.y[1]};\n')
        if self.position != '':
            param = [self.position + ';\n'] + param
        for i in range(0, len(param)):
            param[i] = '\t\t\t\t' + param[i]

        self.style = [head] + param + [close]

    def set_code(self):
        self.main_code = [f'<img class="c{self.index}" src="{self.src}"\n', f'\t alt="{self.alt}"\n',
                          f'\t width={self.width[0]}{self.width[1]}\n',
                          f'\t height={self.height[0]}{self.height[1]}>\n']
        for i in range(0, len(self.main_code)):
            self.main_code[i] = '\t\t' + self.main_code[i]
        self.cryptographer()


class Rect:
    def __init__(self, x, y, width, height, border, border_color, color, index, name, start_obj=None, rel=-1):
        self.type = 'element'
        self.rel = rel
        self.x = [x[0], x[1]]
        self.y = [y[0], y[1]]
        self.x_code = [x[0], x[1]]
        self.y_code = [y[0], y[1]]
        self.w = width
        self.h = height
        self.border = border
        self.border_color = border_color
        self.color = color
        self.index = index
        self.style = []
        self.main_code = []
        self.cipher = ''
        self.name = name
        self.start_obj = start_obj

    def cryptographer(self):
        self.cipher = f'{rect_mark}&' + \
                      f'{str(self.x_code[0])}^{self.x_code[1]}&' + \
                      f'{str(self.y_code[0])}^{self.y_code[1]}&' + \
                      f'{self.w[0]}^{self.w[1]}&' + \
            f'{self.h[0]}^{self.h[1]}&{self.border[0]}^{self.border[1]}&{self.border_color}&{self.color}&{self.name}'
        self.cipher += f'&{self.rel}'
        self.cipher = '\t\t<!--' + self.cipher + '-->\n'
        self.main_code = [self.cipher] + self.main_code

    def set_style(self):
        param = []
        head = f'.c{self.index}' + '{\n'
        close = '}\n'
        param.append(f'position:absolute;\n')
        if self.start_obj is not None:
            self.x[0] = f'calc({self.x_code[0]}{self.x_code[1]} + {self.start_obj.x[0]}{self.start_obj.x[1]})'
            self.x[1] = ''
            self.y[0] = f'calc({self.y_code[0]}{self.y_code[1]} + {self.start_obj.y[0]}{self.start_obj.y[1]})'
            self.y[1] = ''
        param.append(f'left:{self.x[0]}{self.x[1]};\n')
        param.append(f'top:{self.y[0]}{self.y[1]};\n')
        param.append(f'width:{self.w[0]}{self.w[1]};\n')
        param.append(f'height:{self.h[0]}{self.h[1]};\n')
        param.append(f'border:{self.border[0]}{self.border[1]} solid {self.border_color};\n')
        param.append(f'background-color:{self.color};\n')
        for i in range(0, len(param)):
            param[i] = '\t' + param[i]

        self.style = [head] + param + [close]
        for i in range(0, len(self.style)):
            self.style[i] = '\t\t\t' + self.style[i]

    def set_code(self):
        self.main_code = [f'\t\t<div class="c{self.index}">', '</div>\n']
        self.cryptographer()


class Oval:
    def __init__(self, x, y, width, height, border, border_color, color, index, name, start_obj, rel):
        self.x = [x[0], x[1]]
        self.y = [y[0], y[1]]
        self.rel = rel
        self.x_code = [x[0], x[1]]
        self.y_code = [y[0], y[1]]
        self.w = width
        self.h = height
        self.border = border
        self.border_color = border_color
        self.color = color
        self.index = index
        self.position = ''
        self.style = []
        self.main_code = []
        self.type = 'element'
        self.cipher = ''
        self.name = name
        self.start_obj = start_obj

    def cryptographer(self):
        self.cipher = f'{oval_mark}&' + \
                      f'{str(self.x_code[0])}^{self.x_code[1]}&' + \
                      f'{str(self.y_code[0])}^{self.y_code[1]}&' + \
                      f'{self.w[0]}^{self.w[1]}&' + \
            f'{self.h[0]}^{self.h[1]}&{self.border[0]}^{self.border[1]}&{self.border_color}&{self.color}&{self.name}'
        self.cipher += f'&{self.rel}'
        self.cipher = '\t\t<!--' + self.cipher + '-->\n'
        self.main_code = [self.cipher] + self.main_code

    def set_style(self):
        param = []
        head = f'.c{self.index}' + '{\n'
        close = '}\n'
        param.append(f'position:absolute;\n')
        if self.start_obj is not None:
            self.x[0] = f'calc({self.x_code[0]}{self.x_code[1]} + {self.start_obj.x[0]}{self.start_obj.x[1]})'
            self.x[1] = ''
            self.y[0] = f'calc({self.y_code[0]}{self.y_code[1]} + {self.start_obj.y[0]}{self.start_obj.y[1]})'
            self.y[1] = ''
        param.append(f'left:{self.x[0]}{self.x[1]};\n')
        param.append(f'top:{self.y[0]}{self.y[1]};\n')
        param.append(f'width:{self.w[0]}{self.w[1]};\n')
        param.append(f'height:{self.h[0]}{self.h[1]};\n')
        param.append(f'border:{self.border[0]}{self.border[1]} solid {self.border_color};\n')
        param.append(f'background-color:{self.color};\n')
        param.append('border-radius:50%;\n')
        for i in range(0, len(param)):
            param[i] = '\t' + param[i]

        self.style = [head] + param + [close]
        for i in range(0, len(self.style)):
            self.style[i] = '\t\t\t' + self.style[i]

    def set_code(self):
        self.main_code = [f'\t\t<div class="c{self.index}">', '</div>\n']
        self.cryptographer()


class Pen:
    def __init__(self, points, width, color, index, name, start_obj, rel):
        self.type = 'lines'
        self.rel = rel
        self.points = points
        self.p2 = points
        self.width = width
        self.color = color
        self.index = index
        self.style = []
        self.main_code = []
        self.cipher = ''
        self.name = name
        self.start_obj = start_obj

    def cryptographer(self):
        self.cipher = f'\t\t<!--{line_mark}&{self.width}&{self.color}&{self.name}&{self.rel}-->\n'
        st = ''
        for p in self.p2:
            st += f'{p[0]}^{p[1]}&'
        self.cipher += '\t\t<!--' + st[0:-1] + '-->\n'
        self.main_code = [self.cipher] + self.main_code

    def set_style(self):
        self.style = []

    def set_code(self):
        if self.start_obj is not None:
            x = self.start_obj.x
            y = self.start_obj.y
            dx = x[0]
            dy = y[0]
            if x[1] == 'vw':
                dx = f'{dx / 100}*window.innerWidth'
            if x[1] == 'vh':
                dx = f'{dx / 100}*window.innerHeight'
            if x[1] == '':
                dx = Pen.translate(dx)
            if y[1] == 'vw':
                dy = f'{dy / 100}*window.innerWidth'
            if y[1] == 'vh':
                dy = f'{dy / 100}*window.innerHeight'
            if y[1] == '':
                dy = Pen.translate(dy)
            self.points = list(map(lambda p: [f'{dx}+{p[0]}', f'{dy}+{p[1]}'], self.p2))
        self.main_code = [f'\t\t<div class = "c{self.index}">', '<script>\n']
        self.main_code += [f'\t\t\tctx.beginPath();\n']
        self.main_code += [f'\t\t\tif({self.points[0][0]} > canvas.width)canvas.width = {self.points[0][0]};\n']
        self.main_code += [f'\t\t\tif({self.points[0][1]} > canvas.height)canvas.height = {self.points[0][1]};\n']
        self.main_code.append(f'\t\t\tctx.moveTo({self.points[0][0]}, {self.points[0][1]});\n')
        for i in range(1, len(self.points)):
            self.main_code += [f'\t\t\tif({self.points[i][0]} > canvas.width)canvas.width = {self.points[i][0]};\n']
            self.main_code += [f'\t\t\tif({self.points[i][1]} > canvas.height)canvas.height = {self.points[i][1]};\n']
            self.main_code.append(f'\t\t\tctx.lineTo({self.points[i][0]}, {self.points[i][1]});\n')
        self.main_code.append(f'\t\t\tctx.strokeStyle = "{self.color}";\n')
        self.main_code.append(f'\t\t\tctx.lineWidth = "{self.width}";\n')
        self.main_code.append('\t\t\tctx.stroke();\n')
        self.main_code += [f'\t\t\tctx.closePath();\n']
        self.main_code.append('\t\t</script></div>\n')
        self.cryptographer()

    @staticmethod
    def translate(s):
        if s[0] == 'c':
            return Pen.translate(s[5:-1])
        s1 = s.split('+')
        if len(s1) == 1:
            if s1[0][-2] == 'h':
                s1[0] = f'{int(s1[0][0:-3]) / 100}*window.innerHeight'
            elif s1[0][-2] == 'w':
                s1[0] = f'{int(s1[0][0:-3]) / 100}*window.innerWidth'
            elif s1[0][-2] == 'x':
                s1[0] = s1[0][0:-3]
            elif s1[0][-2] == 't':
                s1[0] = str(int(s1[0][0:-3])*4/3)
            return s1
        if len(s1) == 2:
            if s1[0][-2] == 'h':
                s1[0] = f'{int(s1[0][0:-3]) / 100}*window.innerHeight'
            elif s1[0][-2] == 'w':
                s1[0] = f'{int(s1[0][0:-3]) / 100}*window.innerWidth'
            elif s1[0][-2] == 'x':
                s1[0] = s1[0][0:-3]
            elif s1[0][-2] == 't':
                s1[0] = str(int(s1[0][0:-3])*4/3)
            if s1[1][-1] == 'h':
                s1[1] = f'{int(s1[1][1:-2]) / 100}*window.innerHeight'
            elif s1[1][-1] == 'w':
                s1[1] = f'{int(s1[1][1:-2]) / 100}*window.innerWidth'
            elif s1[1][-1] == 'x':
                s1[1] = s1[1][1:-2]
            elif s1[1][-1] == 't':
                s1[1] = str(int(s1[1][1:-2])*4/3)
            return f'{s1[0]}+{s1[1]}'

        if s1[0][-2] == 'h':
            s1[0] = f'{int(s1[0][0:-3]) / 100}*window.innerHeight'
        if s1[0][-2] == 'w':
            s1[0] = f'{int(s1[0][0:-3]) / 100}*window.innerWidth'
        if s1[0][-2] == 'x':
            s1[0] = s1[0][0:-3]
        return f'{s1[0]}+{Pen.translate(s[len(s1[0]) + 5:])}'


class Icon:
    def __init__(self, icon):
        self.main_code = []
        self.type = 'heading'
        self.style = []
        self.icon = icon
        self.cipher = ''

    def cryptographer(self):
        self.cipher = f'\t\t<!--{icon_mark} {self.icon}-->\n'
        self.main_code = [self.cipher] + self.main_code

    def set_code(self):
        self.main_code = [f'\t\t<link rel = "icon" href = "{self.icon}" type = "image/x-icon">\n']
        self.cryptographer()


class Title:
    def __init__(self, title):
        self.type = 'heading'
        self.title = title
        self.cipher = ''
        self.main_code = []
        self.style = []

    def cryptographer(self):
        self.cipher = f'\t\t<!--{title_mark} {self.title}-->\n'
        self.main_code = [self.cipher] + self.main_code

    def set_code(self):
        self.main_code = ['\t\t<title>', self.title, '</title>\n']
        self.cryptographer()


class SiteBuilder:

    def __init__(self, file=''):
        self.code = []
        self.prev = []
        self.ind_class = int(0)
        self.parent_index = []
        self.page_icon = []
        self.page_title = []
        self.canvas = ['<canvas id="example"></canvas>\n', '<script>\n',
                       '\twindow.canvas = document.getElementById("example");\n',
                       f'\twindow.ctx = canvas.getContext(\'2d\');\n',
                       '\twindow.canvas.width = window.innerWidth;\n',
                       '\twindow.canvas.height = window.innerHeight;\n', '</script>\n']
        self.canvas = list(map(lambda s: '\t\t' + s, self.canvas))

        self.determine()
        if file == '':
            return
        comments = SiteBuilder.open_proj(f'{file}.html')
        if comments[0] != heading_mark:
            return
        t = False
        t2 = False
        for i in range(0, len(comments)):
            if t is True:
                t = False
                continue
            if t2 is True:
                t2 = False
                continue
            com = str(comments[i])
            com = com[4:-3]
            words = com.split('&')
            if words[0] == paragraph_mark:
                text = comments[i+1][4:-3]
                links = comments[i+2][4:-3]
                self.read_paragraph(words=words[1:], text=text, links=links)
                t = True
                t2 = True
            if words[0] == image_mark:
                self.read_image(words[1:])
            if words[0] == rect_mark:
                self.read_rect(words[1:])
            if words[0] == oval_mark:
                self.read_oval(words[1:])
            if words[0] == tab_mark:
                self.read_caption(words[1:])
            if words[0] == icon_mark:
                self.icon(link=words[1])
            if words[0] == title_mark:
                self.title(text=words[1])
            if words[0] == line_mark:
                points = comments[i+1][4:-3]
                self.read_lines(words=words[1:], points=points)
                t = True
            if words[0] == number_mark:
                self.ind_class = words[1]

    @staticmethod
    def open_proj(html_file):
        with open(html_file, 'r', encoding='UTF-8') as file:
            cipher = list(map(lambda x: x.strip(),
                              filter(lambda x: x if '<!--' in x and '-->' in x else None, file.readlines())))

        return cipher

    def read_paragraph(self, words, text, links):
        x = words[0].split('^')
        y = words[1].split('^')
        font_size = words[5].split('^')
        font = words[4]
        color = words[3]
        width = words[2].split('^')
        name = words[6]
        rel = int(words[7])
        self.paragraph(text=text, x=x, y=y, width=width, font_size=font_size, font=font, color=color, name=name,
                       rel_index=rel, links=links)

    def read_image(self, words):
        src = words[0]
        x = words[1].split('^')
        y = words[2].split('^')
        w = words[3].split('^')
        h = words[4].split('^')
        alt = words[5]
        name = words[6]
        rel = int(words[7])
        self.image(src=src, width=w, height=h, x=x, y=y, alt=alt, name=name, rel_index=rel)

    def read_rect(self, words):
        x = words[0].split('^')
        y = words[1].split('^')
        w = words[2].split('^')
        h = words[3].split('^')
        border = words[4].split('^')
        b_c = words[5]
        color = words[6]
        name = words[7]
        rel = int(words[8])
        self.square(x=x, y=y, width=w, height=h, border_color=b_c,  border=border, color=color, name=name,
                    rel_index=rel)

    def read_oval(self, words):
        x = words[0].split('^')
        y = words[1].split('^')
        w = words[2].split('^')
        h = words[3].split('^')
        border = words[4].split('^')
        b_c = words[5]
        color = words[6]
        name = words[7]
        rel = int(words[8])
        self.oval(x=x, y=y, width=w, height=h, border_color=b_c,  border=border, color=color, name=name, rel_index=rel)

    def read_caption(self, words):
        p_n = words[0]
        icon = words[1]
        self.tab(page_name=p_n, icon=icon)

    def read_lines(self, words, points):
        w = (words[0], 'px')
        color = words[1]
        p = list(map(lambda x: [x[0], 'px', x[1], 'px'], map(lambda x: x.split('^'), points.split('&'))))
        name = words[2]
        rel = int(words[3])
        self.pen(points=p, width=w, color=color, name=name, rel_index=rel)

    def determine(self):
        self.code = [heading_mark + '\n', '<!DOCTYPE html>\n', '<html>\n', "\t<head>\n", self.page_icon,
                     self.page_title,
                     '\t\t<style>\n', '\t\t</style>\n', '\t\t<meta charset = "utf-8">\n', '\t</head>\n', '\t<body>\n',
                     '\t</body>\n', '</html>\n', f'<!--{number_mark} {self.ind_class}-->']

    def tab(self, page_name, icon):
        self.icon(link=icon)
        self.title(text=page_name)

    def icon(self, link):
        s = Icon(link)
        s.set_code()
        self.page_icon = s.main_code

    def title(self, text):
        s = Title(text)
        s.set_code()
        self.page_title = s.main_code

    def paragraph(self, text, font_size, x, y, width, font, name, links=[], num=-1, color='black', rel_index=-1,
                  change=False):
        w = [width[0], width[1]]

        start_obj = None
        if rel_index > -1:
            start_obj = self.prev[rel_index]
        s = Paragraph(text=text, font_size=font_size, x=x,
                      y=y, width=w, color=color, font=font,
                      index=self.ind_class, links=links, name=name, start_obj=start_obj, rel=rel_index)

        if change is True:
            self.insert(s, num)
            return
        self.prev.append(s)
        self.parent_index.append(rel_index)
        self.ind_class += 1
        self.replace(from_index=-1, to_index=num)

    def image(self, src, width, height, x, y, name, alt='picture', num=-1, rel_index=-1, change=False):
        start_obj = None
        if rel_index > -1:
            start_obj = self.prev[rel_index]
        s = Image(src=src, x=x, y=y, width=width, height=height, index=self.ind_class, alt=alt, name=name,
                  start_obj=start_obj, rel=rel_index)

        if change is True:
            self.insert(s, num)
            return
        self.prev.append(s)
        self.parent_index.append(rel_index)
        self.ind_class += 1
        self.replace(from_index=-1, to_index=num)

    def square(self, x, y, width, height, border, name, color='', border_color='', num=-1, rel_index=-1, change=False):
        if color == '':
            color = 'black'
        if border_color == '':
            border_color = 'black'
        b = [border[0], border[1]]
        if b[0] == '':
            b[0] = 0
            b[1] = 'px'
        start_obj = None
        if rel_index > -1:
            start_obj = self.prev[rel_index]
        s = Rect(x=x, y=y, width=width, height=height, border=b, border_color=border_color, color=color,
                 index=self.ind_class, name=name, start_obj=start_obj, rel=rel_index)

        if change is True:
            self.insert(s, num)
            return
        self.ind_class = 1 + int(self.ind_class)
        self.prev.append(s)
        self.parent_index.append(rel_index)
        self.replace(from_index=-1, to_index=num)

    def oval(self, x, y, width, height, border, color, name, border_color='', num=-1, rel_index=-1, change=False):
        if color == '':
            color = 'black'
        if border_color == '':
            border_color = 'black'
        b = [border[0], border[1]]
        if b[0] == '':
            b[0] = 0
        start_obj = None
        if rel_index > -1:
            start_obj = self.prev[rel_index]
        s = Oval(x=x, y=y, width=width, height=height, border=b, border_color=border_color, color=color,
                 index=self.ind_class, name=name, start_obj=start_obj, rel=rel_index)

        if change is True:
            self.insert(s, num)
            return
        self.ind_class += 1
        self.prev.append(s)
        self.parent_index.append(rel_index)
        self.replace(from_index=-1, to_index=num)

    def pen(self, points, width, color, name, num=-1, rel_index=-1, change=False):
        start_obj = None
        if color == '':
            color = 'black'
        w = width[0]
        if width[1] == 'vw':
            w = f'{w / 100}*window.innerWidth'
        if width[1] == 'vh':
            w = f'{w / 100}*window.innerHeight'
        if rel_index > -1:
            start_obj = self.prev[rel_index]
        p = []
        for i in range(0, len(points)):
            x = points[i][0]
            y = points[i][2]
            if points[i][1] != 'px':
                x = f'{x/100}*window.innerWidth'
            if points[i][3] != 'px':
                y = f'{y/100}*window.innerHeight'
            p += [(x, y)]
        s = Pen(points=p, width=w, color=color, index=self.ind_class, name=name, start_obj=start_obj, rel=rel_index)

        if change is True:
            self.insert(s, num)
            return
        self.ind_class += 1
        self.prev.append(s)
        self.parent_index.append(rel_index)
        self.replace(from_index=-1, to_index=num)

    def print_code(self):
        self.determine()
        index_style = self.code.index('\t\t</style>\n')
        index_body = self.code.index('\t</body>\n')
        styles = []
        codes = []
        for i in range(0, len(self.prev)):
            if self.prev[i].type == 'heading':
                continue
            if self.parent_index[i] > -1:
                self.prev[i].start_obj = self.prev[self.parent_index[i]]
            self.prev[i].set_style()
            self.prev[i].set_code()
            styles.append(self.prev[i].style)
            codes.append(self.prev[i].main_code)

        self.code = self.code[0:index_style] + styles + \
            self.code[index_style:index_body] + codes + self.code[index_body:]
        b = self.code.index('\t<body>\n') + 1
        self.code = self.code[0: b] + self.canvas + self.code[b:]

    def save(self, html):
        self.print_code()
        with open(f'{html}', 'w', encoding='UTF-8') as file:
            for cod in self.code:
                file.writelines(cod)

    def replace(self, from_index, to_index):
        if from_index == to_index:
            return
        step = self.prev[from_index]
        del self.prev[from_index]
        self.prev = self.prev[0:to_index] + [step] + self.prev[to_index:]
        step = self.parent_index[from_index]
        del self.parent_index[from_index]
        self.parent_index = self.parent_index[0:to_index] + [step] + self.parent_index[to_index:]

    def undo(self, index):
        if index < 0:
            index += len(self.prev)
        for i in range(len(self.prev)-1, -1, -1):
            if self.parent_index[i] == index:
                self.undo(i)
        del self.prev[index]
        del self.parent_index[index]

    def insert(self, action, num):
        if action.__class__.__name__ != self.prev[num].__class__.__name__:
            raise Exception('Another class')
        self.prev[num] = action
        self.parent_index[num] = action.rel
        self.ind_class += 1

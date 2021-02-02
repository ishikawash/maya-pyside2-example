# -*- coding: utf-8 -*-

# Resource object code
#
# Created: 火 2 2 09:22:37 2021
#      by: The Resource Compiler for PySide2 (Qt v5.12.5)
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = "\
\x00\x00\x06x\
<\
?xml version=\x221.\
0\x22 encoding=\x22UTF\
-8\x22?>\x0d\x0a<ui versi\
on=\x224.0\x22>\x0d\x0a <cla\
ss>MainWindow</c\
lass>\x0d\x0a <widget \
class=\x22QMainWind\
ow\x22 name=\x22MainWi\
ndow\x22>\x0d\x0a  <prope\
rty name=\x22geomet\
ry\x22>\x0d\x0a   <rect>\x0d\
\x0a    <x>0</x>\x0d\x0a \
   <y>0</y>\x0d\x0a   \
 <width>200</wid\
th>\x0d\x0a    <height\
>150</height>\x0d\x0a \
  </rect>\x0d\x0a  </p\
roperty>\x0d\x0a  <pro\
perty name=\x22wind\
owTitle\x22>\x0d\x0a   <s\
tring>MainWindow\
</string>\x0d\x0a  </p\
roperty>\x0d\x0a  <wid\
get class=\x22QWidg\
et\x22 name=\x22centra\
lwidget\x22>\x0d\x0a   <l\
ayout class=\x22QVB\
oxLayout\x22 name=\x22\
verticalLayout_2\
\x22>\x0d\x0a    <item>\x0d\x0a\
     <layout cla\
ss=\x22QVBoxLayout\x22\
 name=\x22verticalL\
ayout\x22>\x0d\x0a      <\
item>\x0d\x0a       <w\
idget class=\x22QLa\
bel\x22 name=\x22label\
\x22>\x0d\x0a        <pro\
perty name=\x22maxi\
mumSize\x22>\x0d\x0a     \
    <size>\x0d\x0a    \
      <width>167\
77215</width>\x0d\x0a \
         <height\
>16777215</heigh\
t>\x0d\x0a         </s\
ize>\x0d\x0a        </\
property>\x0d\x0a     \
   <property nam\
e=\x22font\x22>\x0d\x0a     \
    <font>\x0d\x0a    \
      <pointsize\
>32</pointsize>\x0d\
\x0a         </font\
>\x0d\x0a        </pro\
perty>\x0d\x0a        \
<property name=\x22\
text\x22>\x0d\x0a        \
 <string>Hello !\
</string>\x0d\x0a     \
   </property>\x0d\x0a\
        <propert\
y name=\x22alignmen\
t\x22>\x0d\x0a         <s\
et>Qt::AlignCent\
er</set>\x0d\x0a      \
  </property>\x0d\x0a \
      </widget>\x0d\
\x0a      </item>\x0d\x0a\
      <item>\x0d\x0a  \
     <widget cla\
ss=\x22QPushButton\x22\
 name=\x22pushButto\
n\x22>\x0d\x0a        <pr\
operty name=\x22tex\
t\x22>\x0d\x0a         <s\
tring>OK</string\
>\x0d\x0a        </pro\
perty>\x0d\x0a       <\
/widget>\x0d\x0a      \
</item>\x0d\x0a     </\
layout>\x0d\x0a    </i\
tem>\x0d\x0a   </layou\
t>\x0d\x0a  </widget>\x0d\
\x0a  <widget class\
=\x22QMenuBar\x22 name\
=\x22menubar\x22>\x0d\x0a   \
<property name=\x22\
geometry\x22>\x0d\x0a    \
<rect>\x0d\x0a     <x>\
0</x>\x0d\x0a     <y>0\
</y>\x0d\x0a     <widt\
h>200</width>\x0d\x0a \
    <height>21</\
height>\x0d\x0a    </r\
ect>\x0d\x0a   </prope\
rty>\x0d\x0a  </widget\
>\x0d\x0a  <widget cla\
ss=\x22QStatusBar\x22 \
name=\x22statusbar\x22\
/>\x0d\x0a </widget>\x0d\x0a\
 <resources/>\x0d\x0a \
<connections/>\x0d\x0a\
</ui>\x0d\x0a\
"

qt_resource_name = "\
\x00\x02\
\x00\x00\x07\xb9\
\x00u\
\x00i\
\x00\x0d\
\x03\xb6_y\
\x00M\
\x00a\x00i\x00n\x00w\x00i\x00n\x00d\x00o\x00w\x00.\x00u\x00i\
"

qt_resource_struct = "\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()

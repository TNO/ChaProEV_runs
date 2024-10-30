# **ChaProEV runs**




<center>
<img src=MOPO_logo_chaproev.svg>
</center>

<center>
<img src=ChaProEV_overview.svg>
</center>


This repository contains runs with the ChaProEV model

## Authors and contact
Omar Usmani (Omar.Usmani@TNO.nl)


## Licence

ChaProEV is released under the Apache 2.0 license.
All accompanying documentation and manual are released under the 
Creative Commons BY-SA 4.0 license.


## Installation and use


You can install ChaProEV with pip:
```
pip install ChaProEV
```
And the import ChaProEV in your code.
You can of course use the various functions of ChaProEV, but the general
use case is to run th model and focus on defining your case through the
scenarios and their variants.
In that case, the only piece of code you need is as follows (you just need
to put the name of the folder where you put your case scenarios instead of the
'Mopo'  example).
```python
from ChaProEV import ChaProEV

if __name__ == '__main__':
    case_name: str = 'Mopo'
    ChaProEV.run_ChaProEV(case_name)
```
## Acknowledgments
&nbsp;
<hr>
<center>
<table width=500px frame="none">
<tr>
<td valign="middle" width=100px>
<img src=eu-emblem-low-res.jpg alt="EU emblem" width=100%></td>
<img src=MOPO_logo_main.svg width = 25%>
<td valign="middle">This project was partly develop under funding from 
European Climate, 
Infrastructure and Environment Executive Agency under the European Union’s 
HORIZON Research and Innovation Actions under grant agreement N°101095998.</td>
<tr>
</table>
</center>
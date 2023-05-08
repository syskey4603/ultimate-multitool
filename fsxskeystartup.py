import pystyle
from pystyle import Colorate, Colors, System, Center, Write, Anime
riot = '''
    ..      ...        .                     s
 :~"8888x :"%888x     @88>                  :8
8    8888Xf  8888>    %8P          u.      .88
88x. ?8888k  8888X     .     ...ue888b    :888ooo
8888L'8888X  '%88X   .@88u   888R Y888r -*8888888
"888X 8888X:xnHH(`` ''888E`  888R I888>   8888
  ?8~ 8888X X8888     888E   888R I888>   8888
-~`   8888> X8888     888E   888R I888>   8888
:H8x  8888  X8888     888E  u8888cJ888   .8888Lu=
8888> 888~  X8888     888&   "*888*P"    ^%888*
48"` '8*~   `8888!`   R888"    'Y"         'Y"
 ^-==""      `""       ""'''[1:]


banner = r'''
 n                                                                 :.
 E%                                                                :"5
z  %                                                              :" `
K   ":                                                           z   R
?     %.                                                       :^    J
 ".    ^s                                                     f     :~
  '+.    #L                                                 z"    .*
    '+     %L                                             z"    .~
      ":    '%.                                         .#     +
        ":    ^%.                                     .#`    +"
          #:    "n                                  .+`   .z"
            #:    ":                               z`    +"
              %:   `*L                           z"    z"
                *:   ^*L                       z*   .+"
                  "s   ^*L                   z#   .*"
                    #s   ^%L               z#   .*"
                      #s   ^%L           z#   .r"
                        #s   ^%.       u#   .r"
                          #i   '%.   u#   .@"
                            #s   ^%u#   .@"
                              #s x#   .*"
                               x#`  .@%.
                             x#`  .d"  "%.
                           xf~  .r" #s   "%.
                     u   x*`  .r"     #s   "%.  x.
                     %Mu*`  x*"         #m.  "%zX"
                     :R(h x*              "h..*dN.
                   u@NM5e#>                 7?dMRMh.
                 z$@M@$#"#"                 *""*@MM$hL
               u@@MM8*                          "*$M@Mh.
             z$RRM8F"                             "N8@M$bL
            5`RM$#                                  'R88f)R
            'h.$"                                     #$x*'''[1:]


System.Clear()
System.Size(150, 50)
System.Title("Riot")


Anime.Fade(Center.Center(banner), Colors.blue_to_cyan,
           Colorate.Vertical, enter=True)

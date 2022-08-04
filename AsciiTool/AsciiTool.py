"""##########################
    Txt and Image to Ascii generator
    Developed by: $echo
    Credits: www.figlet.org
   ##########################""" 






import ascii_magic as ac
import pyfiglet as p
import sys
Examples = """Font: 3-d
 ****     ****                  
/**/**   **/**                  
/**//** ** /**  ******   ****** 
/** //***  /** **////** **////**
/**  //*   /**/**   /**/**   /**
/**   /    /**/**   /**/**   /**
/**        /**//****** //****** 
//         //  //////   //////  



Font: 3x5
            
# #         
### ### ### 
### # # # # 
# # ### ### 
# #         



Font: 5lineoblique
                                    
                                    
    /|    //| |                     
   //|   // | |     ___      ___    
  // |  //  | |   //   ) ) //   ) ) 
 //  | //   | |  //   / / //   / /  
//   |//    | | ((___/ / ((___/ /   



Font: acrobatic
  o          o                            
 <|\        /|>                           
 / \\o    o// \                           
 \o/ v\  /v \o/    o__ __o      o__ __o   
  |   <\/>   |    /v     v\    /v     v\  
 / \        / \  />       <\  />       <\ 
 \o/        \o/  \         /  \         / 
  |          |    o       o    o       o  
 / \        / \   <\__ __/>    <\__ __/>  
                                          
                                          
                                          



Font: alligator
        :::   :::   ::::::::  :::::::: 
      :+:+: :+:+: :+:    :+::+:    :+: 
    +:+ +:+:+ +:++:+    +:++:+    +:+  
   +#+  +:+  +#++#+    +:++#+    +:+   
  +#+       +#++#+    +#++#+    +#+    
 #+#       #+##+#    #+##+#    #+#     
###       ### ########  ########       



Font: alligator2
::::    ::::  ::::::::  ::::::::  
+:+:+: :+:+:+:+:    :+::+:    :+: 
+:+ +:+:+ +:++:+    +:++:+    +:+ 
+#+  +:+  +#++#+    +:++#+    +:+ 
+#+       +#++#+    +#++#+    +#+ 
#+#       #+##+#    #+##+#    #+# 
###       ### ########  ########  



Font: alphabet
M   M         
MM MM         
M M M ooo ooo 
M   M o o o o 
M   M ooo ooo 
              
              



Font: avatar
 _      ____  ____ 
/ \__/|/  _ \/  _ \\
| |\/||| / \|| / \|
| |  ||| \_/|| \_/|
\_/  \|\____/\____/
                   



Font: banner
#     #               
##   ##  ####   ####  
# # # # #    # #    # 
#  #  # #    # #    # 
#     # #    # #    # 
#     # #    # #    # 
#     #  ####   ####  
                      



Font: banner3-D
'##::::'##::'#######:::'#######::
 ###::'###:'##.... ##:'##.... ##:
 ####'####: ##:::: ##: ##:::: ##:
 ## ### ##: ##:::: ##: ##:::: ##:
 ##. #: ##: ##:::: ##: ##:::: ##:
 ##:.:: ##: ##:::: ##: ##:::: ##:
 ##:::: ##:. #######::. #######::
..:::::..:::.......::::.......:::



Font: banner3
##     ##  #######   #######  
###   ### ##     ## ##     ## 
#### #### ##     ## ##     ## 
## ### ## ##     ## ##     ## 
##     ## ##     ## ##     ## 
##     ## ##     ## ##     ## 
##     ##  #######   #######  



Font: banner4
.##.....##..#######...#######.
.###...###.##.....##.##.....##
.####.####.##.....##.##.....##
.##.###.##.##.....##.##.....##
.##.....##.##.....##.##.....##
.##.....##.##.....##.##.....##
.##.....##..#######...#######.



Font: barbwire
><<       ><<                    
>< ><<   ><<<                    
><< ><< > ><<   ><<       ><<    
><<  ><<  ><< ><<  ><<  ><<  ><< 
><<   ><  ><<><<    ><<><<    ><<
><<       ><< ><<  ><<  ><<  ><< 
><<       ><<   ><<       ><<    
                                 



Font: basic
.88b  d88.  .d88b.   .d88b.  
88'YbdP`88 .8P  Y8. .8P  Y8. 
88  88  88 88    88 88    88 
88  88  88 88    88 88    88 
88  88  88 `8b  d8' `8b  d8' 
YP  YP  YP  `Y88P'   `Y88P'  
                             
                             



Font: bell
 __   __              
 |    |    __.    __. 
 |\  /|  .'   \ .'   \\
 | \/ |  |    | |    |
 /    /   `._.'  `._.'
                      



Font: big
 __  __             
|  \/  |            
| \  / | ___   ___  
| |\/| |/ _ \ / _ \ 
| |  | | (_) | (_) |
|_|  |_|\___/ \___/ 
                    
                    



Font: bigchief
______________________
    _   _             
    /  /|             
---/| /-|----__----__-
  / |/  |  /   ) /   )
_/__/___|_(___/_(___/_
                      
                      



Font: binary
01001101 01101111 01101111 



Font: block
                                
_|      _|                      
_|_|  _|_|    _|_|      _|_|    
_|  _|  _|  _|    _|  _|    _|  
_|      _|  _|    _|  _|    _|  
_|      _|    _|_|      _|_|    
                                
                                



Font: bubble
  _   _   _  
 / \ / \ / \ 
( M | o | o )
 \_/ \_/ \_/ 

############################################################
For more Exmaples visit: http://www.figlet.org/examples.html
############################################################
"""
def main():
    if sys.argv[1] == "--help":
        print("""Hello!
        Welocme to the AsciiTool!
        to See the List of Fonts use --list
        to Convert a Text to Ascii use --convert <text> Font: <font>
        to Convert a File to Ascii use --convertFile <file> <font>, Please Pay attention that file in the same path as the tool path!
        to Convert a Image to Ascii use --convertImage <image>, Please Pay attention that image in the same path as the tool path!
        """)
    elif sys.argv[1] == "--list":
        print(Examples)
    elif sys.argv[1] == "--convert":
        txt = []
        for i in range(len(sys.argv)):
            if sys.argv[i] == "Font:":
                Font = sys.argv[i+1]
        for i in range(2, len(sys.argv)):
            if sys.argv[i] == "Font:":
                break
            txt.append(sys.argv[i])
        txt = " ".join(txt)
        print(p.figlet_format(txt, font=Font))
    elif sys.argv[1] == "--convertFile":
        File = open(sys.argv[2], "r")
        TextInFile = File.read()
        File = open(sys.argv[2], "w")
        File.close()
        File = open(sys.argv[2], "a")
        File.write(p.figlet_format(TextInFile, font=sys.argv[3]))
        print("Done!")
    elif sys.argv[1] == "--convertImage":
        Output = ac.from_image_file(sys.argv[2], columns=100, char="#")
        ac.to_terminal(Output)

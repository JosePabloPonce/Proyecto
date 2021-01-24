
def gracias():
    return "\n¡Gracias por tu apoyo, te veremos en la colecta!"

def mundo():
    print("             _-o+&&*....?d:>b\_")
    print("          _o/.`..  ..,, dMF9MMMMMHo_")
    print("       .o&+.        `.MbHMMMMMMMMMMMHo.")
    print("     .o.. .         vodM*$&&HMMMMMMMMMM?.")
    print("    ,.              $M&ood,~..!&++MMMMMMH\"")
    print("   /               ,MMMMMMM+b?+bobMMMMHMMML")
    print("  &              ?MMMMMMMMMMMMMMMMM7MMM$R*Hk")
    print(" ?$.            :MMMMMMMMMMMMMMMMMMM/HMMM|`*L")
    print("|               |MMMMMMMMMMMMMMMMMMMMbMH.   T,")
    print("$H+:            `             MMMMMMMMb+}.  `?")
    print("]MMH+              RE-Cycler  MMMMMMMMMM.    -")
    print("MMMMMb_            =========  MMMMMMMMP.     :")
    print("HMMMMMMMHo                    MMMMMMMT       .")
    print("?MMMMMMMMP                  9MMMMMMMM}       -")
    print("-?MMMMMMM                  |MMMMMMMMM?,d-    .")
    print(" :|MMMMMM-                 `MMMMMMMT .M|.   :")
    print("  .9MMM[                    &MMMMM*. `.    .")
    print("   :9MMk                    `MMM+.        -")
    print("     &M}                     `          .-")
    print("      `&.                             .")
    print("        `~,   .                     ./")
    print("            . _                  .-")
    print("               .`--._,dd+++pp=...")
    
def guate():

    print('                ₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩')
    print('                ₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩')
    print('         ₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩')
    print('            ₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩')
    print('             ₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩')
    print('              ₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩')
    print('                 ₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩')
    print('                  ₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩')
    print('     ₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩')
    print('   ₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩')
    print('  ₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩')
    print('    ₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩')
    print('    ₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩')
    print('    ₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩AQUI₩₩₩₩₩₩₩₩₩₩₩')
    print('      ₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩')
    print('        ₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩')
    print('          ₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩₩')
    print('')

def guardar(loc, datos):
    nuevoguardado = ','.join(list(datos.values()))
    nuevoguardado += '\n'
    with open('Mascotas.csv', 'a', encoding='utf-8') as f:
        f.write("==================DATO==================")
        f.write(nuevoguardado)
    f.close()
    
    
   

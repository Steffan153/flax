# encoding: stores stuff related to encoding of flax

codepage = "₀₁₂₃₄₅₆₇₈₉\n₊₋∇∆√"
codepage += "⍋⍒∊⊂⊆⊏≡≢⌈⌊⍴⍳≤≠≥⍪"
codepage += " !\"#$%&'()*+,-./"
codepage += "0123456789:;<=>?"
codepage += "@ABCDEFGHIJKLMNO"
codepage += "PQRSTUVWXYZ[\\]^_"
codepage += "`abcdefghijklmno"
codepage += "pqrstuvwxyz{|}~¯"
codepage += "₍₎⊢⊣•¬⋈∞´˝±×φ÷ΣΠ"
codepage += "ÇÐĂĊĠŃŇŚŠŻȦḂḄḊḌḞ"
codepage += "ḲṄṖṚṠṪẎẒẠỌ¨°ʲˀ˘˜"
codepage += "ċżḍḟḷṙịọ⁰¹²³⁴⁵⁶⁷"
codepage += "‶˙ᴰᵈᴹᵐᵠᶲˢᴺᵀᵂᵍᵔᵖᵗ"
codepage += "ᵝᵟ‘’ⁱᐣ⁺⁻⁼ⁿ⌜....."
codepage += "................"
codepage += "................"

assert len(codepage) == 256

def encode(program):
    # encode: encode a flax program in unicode to sbcs
    encoded = ""
    for ch in program:
        encoded += chr(codepage.index(ch))
    return encoded

def decode(program):
    # decode: flax program in sbcs to unicode
    decoded = ""
    for ch in program:
        decoded += codepage[ord(ch)]
    return decoded

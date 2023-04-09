{
    "targets": [
        {
            "target_name": "multi-hashing",
            "sources": [
                "multi-hashing.cc",
				"algos/gr.c",
                "allium.c",
                "bcrypt.c",
                "blake.c",
                "yescrypt/sha256_Y.c",
                "yescrypt/yescrypt-best.c",
                "yescrypt/yescryptcommon.c",
                "boolberry.cc",
                "c11.c",
                "cryptonight.c",
                "cryptonight_fast.c",
                "fresh.c",
                "fugue.c",
                "gost.c",
                "groestl.c",
                "hefty1.c",
                "hsr14.c",
                "keccak.c",
                "lbry.c",
                "Lyra2.c",
                "Lyra2RE.c",
                "Lyra2REV2.c",
                "Lyra2REV3.c",
                "Lyra2Z.c",
                "lyra2z16m330.c",
                "lyra2z330.c",
                "m7.c",
                "magimath.c",
                "minotaur.c",
                "neoscrypt.c",
                "nist5.c",
                "odo.cc",
                "phi1612.c",
                "quark.c",
                "qubit.c",
                "scryptjane.c",
                "scryptn.c",
                "sha1.c",
                "sha256d.c",
                "shavite3.c",
                "skein.c",
                "skunk.c",
                "sm3.c",
                "Sponge.c",
                "tribus.c",
                "whirlpoolx.c",
                "x11.c",
                "x13.c",
                "x15.c",
                "x16r.c",
                "x17.c",
                "x25x.c",
                "xevan.c",
                "zr5.c",
                "sha3/aes_helper.c",
                "sha3/hamsi.c",
                "sha3/KeccakP-800-reference.c",
                "sha3/sph_haval.c",
                "sha3/sph_hefty1.c",
                "sha3/sph_fugue.c",
                "sha3/sph_blake.c",
                
                "sha3/sph_bmw.c",
                "sha3/sph_cubehash.c",
                "sha3/sph_echo.c",
                "sha3/sph_gost.c",
                "sha3/sph_groestl.c",
                "sha3/sph_jh.c",
                "sha3/sph_keccak.c",
                "sha3/sph_luffa.c",
                "sha3/sph_shavite.c",
                "sha3/sph_simd.c",
                "sha3/sph_skein.c",
                "sha3/sph_whirlpool.c",
                "sha3/sph_shabal.c",
                "sha3/sph_ripemd.c",
                "sha3/sph_sha2.c",
                "sha3/sph_sha2big.c",
                "sha3/sph_tiger.c",
                "sph/extra.c",
                "sph/extra.h",
                "sph/lane.h",
                "sph/panama.c"
                "sph/SWIFFTX.h"
                "sph/sph_echo.h",
                "sph/sph_panama.h",
                "sph/sph_shavite.h",
                "sph/sph_whirlpool.h",
                "crypto/aesb.c",
                "crypto/c_blake256.c",
                "crypto/c_groestl.c",
                "crypto/c_jh.c",
                "crypto/c_keccak.c",
                "crypto/c_skein.c",
                "crypto/hash.c",
                "crypto/oaes_lib.c",
                "crypto/odocrypt.cpp",
                "crypto/wild_keccak.cpp",
                "yespower/yespower.c",
                "yespower/yespower-opt.c",
                "heavyhash/heavyhash.c",
                "heavyhash/keccak_tiny.c"

            ],
            'conditions': [
                ['OS=="linux"',
                  {
                    'link_settings': {
                      'libraries': [
                        '-lgmp'
                      ]
                    }
                  }
                ],
                ['OS=="mac"',
                  {
                    'link_settings': {
                      'libraries': [
                        '-lgmp'
                      ]
                    }
                  }
                ],
                ['OS=="win"',
                  {
                    'link_settings': {
                      'libraries': [
                        '-lgmp.lib'
                      ],
                    }
                  }
                ]
              ],
            "include_dirs": [
                "crypto"
            ],
            "cflags_cc": [
                "-std=c++0x"
            ],
        }
    ]
}

#!/usr/bin/env python

import os, sys, json

offsets = [0, 2565047, 2573761, 2582475, 2591189, 2599903, 2608617, 2617331, 2626045, 2634759, 2643473, 2660901, 2669615, 2678329, 2687043, 2695757, 2704471, 2713185, 2721899, 2730613, 2739327, 2748041, 2756755, 2765469, 2774183, 2782897, 2791611, 2800325, 2809039, 2817753, 2826467, 2835181, 2843895, 2852609, 2861323, 2870037, 2878751, 2887465, 2896179, 2904893, 2913607, 2922321, 2931035, 2939749, 2948463, 2957177, 2965891, 2974605, 2983319, 2992033, 3000747, 3009461, 3018175, 3026889, 3035603, 3044317, 3053031, 3061745, 3070459, 3079173, 3087887, 3096601, 3105315, 3114029, 3122743, 3131457, 3140171, 3148885, 3157599, 3166313, 3175027, 3183741, 3192455, 3201169, 3209883, 3218597, 3227311, 3236025, 3244739, 3253453, 3262167, 3270881, 3279595, 3288309, 3297023, 3305737, 3314451, 3323165, 3331879, 3340593, 3349307, 3358021, 3366735, 3375449, 3384163, 3392877, 3401591, 3410305, 3419019, 3427733, 2652187]

size = 0x220a

def write_level_file(level, filepath):
    f = open(filepath, 'w')
    f.write('# %d\n' % level['touchmax'])
    for i in range(6):
        for j in range(5):
            idx = i * 5 + j
            if level['items'][idx] == 0:
                bubble = 0
            else:
                bubble = 5 - level['items'][idx]
            f.write('%d ' % bubble)
        f.write('\n')
    f.close()

def main(asset, outdir):
    if not os.path.exists(outdir):
        os.makedirs(outdir)

    content = open(asset, 'r').read()

    for pack in range(1, 101):
        print('pack %d' % pack)
        json_str = content[offsets[pack]:offsets[pack]+size]
        levels = json.loads(json_str)
        for level in range(len(levels['levels'])):
            write_level_file(levels['levels'][level], os.path.join(outdir, '%d-%d.in' % (pack, level+1)))

    return 0

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('usage: %s <K.WAV> <output-dir>' % sys.argv[0])
        sys.exit(10)
    sys.exit(main(sys.argv[1], sys.argv[2]))

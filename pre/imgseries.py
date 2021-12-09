#!/usr/bin/env python3
# -*- coding: utf8 -*-

import os
import ffmpeg


def imgseries(videofile, output):

    print('Extracting frames from', videofile, 'to directory', output)
    (
        ffmpeg.input(videofile)
        .output(os.path.join(output, 'frame_%06d.jpg'))
        .run()
    )
    for f in range(len(os.listdir(output))):
        old = 'frame_%06d.jpg' % (f+1)
        new = 'frame_%06d.jpg' % f
        print('moving from', os.path.join(output, old), 'to', os.path.join(output, new))
        os.rename(os.path.join(output, old), os.path.join(output, new))
    print('Done.', output)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('videofile', help='Video file')
    parser.add_argument('-o', '--output', help='Output directory')

    args = parser.parse_args()

    if not args.output:
        # split ext
        filename, _ = os.path.splitext(args.videofile)
        args.output = filename + '_frames'

    os.makedirs(args.output, exist_ok=True)

    print(args)

    imgseries(args.videofile, args.output)

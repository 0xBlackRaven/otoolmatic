#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author             : @BlackRaven
# Date created       : 4 Feb 2022
import modNMAP,modVULN
def main():
    modNMAP.main()
    from modNMAP import dir,ip_target
    modVULN.main(dir,ip_target)

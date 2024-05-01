#!/usr/bin/python3
"""Lockbox Solver module"""


def canUnlockAll(boxes):
    """Lockbox Solver"""
    box_map = {i: {"keys": box, "unlocked": False}
               for i, box in enumerate(boxes)}
    box_map[0]["unlocked"] = True
    keys = box_map[0]["keys"]
    for key in keys:
        if key < len(boxes) and not box_map[key]["unlocked"]:
            box_map[key]["unlocked"] = True
            new_keys = [x for x in box_map[key]["keys"] if x not in keys]
            keys += new_keys
    return all(box["unlocked"] for box in box_map.values())

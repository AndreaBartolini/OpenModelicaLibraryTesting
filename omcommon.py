#!/usr/bin/env python3

import html, datetime, re

def friendlyStr(f):
  if f>60:
    return html.escape(str(datetime.timedelta(seconds=int(f))))
  else:
    return html.escape("%.2f" % f)

def multiple_replace(string, *key_values):
  def multiple_replacer(*key_values):
    replace_dict = dict(key_values)
    replacement_function = lambda match: replace_dict[match.group(0)]
    pattern = re.compile("|".join([re.escape(k) for k, v in key_values]), re.M)
    return lambda string: pattern.sub(replacement_function, string)
  return multiple_replacer(*key_values)(string)

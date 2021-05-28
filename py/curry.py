# Copyright Marcus, 2021

from __future__ import annotations
from inspect import signature, Parameter
from typing import *

empty_val = object()

class param:
   """
   type param = Positional of int | Keyword of str | Both of int * str
   """
   def __init__(self, *, ps: Optional[int] = None, kw: Optional[str] = None):
      self.ps = ps
      self.kw = kw

class arg(param):
   def __init__(self, param: param, val, /):
      self.ps  = param.ps
      self.kw  = param.kw
      self.val = val

   def __repr__(self):
      return f"repr{{{self.ps = } {self.kw = } {self.val = }}}"

def curry(fn: Callable) -> curried:
   i = 0
   params = []
   variadic_params = Parameter.VAR_POSITIONAL, Parameter.VAR_KEYWORD
   for name, p in signature(fn).parameters.items():
      if p.kind in variadic_params:
         raise TypeError("Cannot curry variadic parameters!")

      if p.kind == Parameter.POSITIONAL_ONLY:
         params.append(param(ps = i))
         i += 1
         continue

      if p.kind == Parameter.POSITIONAL_OR_KEYWORD:
         params.append(param(ps = i, kw = name))
         i += 1
         continue

      if p.kind == Parameter.KEYWORD_ONLY:
         params.append(param(kw = name))

   return curried(fn, i, params)

class placeholder:
   pass

__ = placeholder()

class curried(Callable):
   def __init__(self, fn: Callable, psargs_len: int, params: list[param], args: list[arg] = []):
      self.fn = fn
      self.params = params
      self.psargs_len = psargs_len
      self.args = args

   # curry functionality
   def __call__(self, *psargs, **kwargs):
      new_params = self.params[:]
      new_args   = self.args[:]

      i = 0
      for psarg in psargs:
         if psarg is __:
            i += 1
            continue

         j = i
         plen = len(new_params)
         found_param = False
         while j < plen:
            if new_params[j].ps is not None:
               found_param = True
               new_args.append(arg(new_params.pop(j), psarg))
               break
            j += 1

         if found_param:
            continue
         raise TypeError("Too many positional arguments!")

      for name, kwarg in kwargs.items():
         if kwarg is __:
            raise TypeError("Placeholder in keyword argument not allowed!")

         found_param = False
         for j, param in enumerate(new_params):
            if param.kw == name:
               found_param = True
               new_args.append(arg(new_params.pop(j), kwarg))
               break

         if not found_param:
            raise TypeError(f"Unexpected keyword argument '{kwarg}'")

      if len(new_params) == 0:
         re_psargs = [None]*self.psargs_len
         re_kwargs = {}
         for re_arg in new_args:
            if re_arg.ps is not None:
               re_psargs[re_arg.ps] = re_arg.val
            else:
               re_kwargs[re_arg.kw] = re_arg.val
         return self.fn(*re_psargs, **re_kwargs)
      else:
         return curried(self.fn, self.psargs_len, new_params, new_args)

   def __matmul__(self, other: Callable):
      def piped(*psargs, **kwargs):
         return other(self.fn(*psargs, **kwargs))
      return curried(piped, self.psargs_len, self.params, self.args)

# -*- mode: python ; coding: utf-8 -*-
import os
import importlib

block_cipher = None


a = Analysis(['maskdetect.py'],
             pathex=['D:\\detectmask'],
             binaries=[],
             datas=[(os.path.join(os.path.dirname(importlib.import_module('tensorflow').__file__),
                              "lite/experimental/microfrontend/python/ops/_audio_microfrontend_op.so"),
                 "tensorflow/lite/experimental/microfrontend/python/ops/"), 
                 ('mask_detector.model', '.'), 
                 ('warning.mp3', '.'), 
                 ('face_detector\\deploy.prototxt', 'face_detector'), 
                 ('face_detector\\res10_300x300_ssd_iter_140000.caffemodel', 'face_detector'), 
                 ('C:\\Python\\Lib\\site-packages\\tensorflow\\python\\_pywrap_tensorflow_internal.pyd', '.')],
             hiddenimports=['tensorflow_core','tensorflow.python.keras.engine.base_layer_v1',
                            'tensorflow.python.ops.numpy_ops'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='maskdetect',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='maskdetect')

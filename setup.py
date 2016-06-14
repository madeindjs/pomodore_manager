#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, os
from cx_Freeze import setup, Executable


# On appelle la fonction setup


#############################################################################
# preparation des options
 
# chemins de recherche des modules
# ajouter d'autres chemins (absolus) si necessaire: sys.path + ["chemin1", "chemin2"]
path = sys.path
 
# options d'inclusion/exclusion des modules
includes = []  # nommer les modules non trouves par cx_freeze
excludes = []
packages = []  # nommer les packages utilises
 
# copier les fichiers non-Python et/ou repertoires et leur contenu:
includefiles = []
 
if sys.platform == "win32":
    pass
    # includefiles += [...] : ajouter les recopies specifiques à Windows
elif sys.platform == "linux2":
    pass
    # includefiles += [...] : ajouter les recopies specifiques à Linux
else:
    pass
    # includefiles += [...] : cas du Mac OSX non traite ici
 
# pour que les bibliotheques binaires de /usr/lib soient recopiees aussi sous Linux
binpathincludes = []
if sys.platform == "linux2":
    binpathincludes += ["/usr/lib"]
 
# niveau d'optimisation pour la compilation en bytecodes
optimize = 0
 
# si True, n'affiche que les warning et les erreurs pendant le traitement cx_freeze
silent = True
 
# construction du dictionnaire des options
options = {"path": path,
           "includes": includes,
           "excludes": excludes,
           "packages": packages,
           "include_files": includefiles,
           "bin_path_includes": binpathincludes,
           "create_shared_zip": False,  # <= ne pas generer de fichier zip
           "include_in_shared_zip": False,  # <= ne pas generer de fichier zip
           "compressed": False,  # <= ne pas generer de fichier zip
           "optimize": optimize,
           "silent": silent
           }
 
# pour inclure sous Windows les dll system de Windows necessaires
if sys.platform == "win32":
    options["include_msvcr"] = True
 
#############################################################################
# preparation des cibles
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # pour application graphique sous Windows
    # base = "Console" # pour application en console sous Windows
 
icone = None
if sys.platform == "win32":
    icone = "icone.ico"
 
cible_1 = Executable(
    script="monprogramme1.pyw",
    base=base,
    compress=False,  # <= ne pas generer de fichier zip
    copyDependentFiles=True,
    appendScriptToExe=True,
    appendScriptToLibrary=False,  # <= ne pas generer de fichier zip
    icon=icone
    )
 
cible_2 = Executable(
    script="monprogramme2.pyw",
    base=base,
    compress=False,
    copyDependentFiles=True,
    appendScriptToExe=True,
    appendScriptToLibrary=False,
    icon=icone
    )
 


setup(
    name = "Pomodore_Manager",
    version = "0.1",
    description = "A simply pomodore manager run with Tkinter & Sqlite3 librairies.",
    author="RousseauAlexandre",
    executables = [Executable("__main__.py")],
)
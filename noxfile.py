# -*- coding: utf-8 -*-
# Copyright © Thomm.o 2020
#
# This file is part of Hikari Command Handler.
#
# Hikari Command Handler is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hikari Command Handler is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Hikari Command Handler. If not, see <https://www.gnu.org/licenses/>.
import nox
import os

PATH_TO_PROJECT = os.path.join(".", "handler")


@nox.session(python=["3.8"])
def format_fix(session):
    session.run("pip", "install", "-U", "black")
    session.run("python", "-m", "black", PATH_TO_PROJECT)


@nox.session(python=["3.8"])
def format(session):
    session.run("pip", "install", "-U", "black")
    session.run("python", "-m", "black", PATH_TO_PROJECT, "--check")

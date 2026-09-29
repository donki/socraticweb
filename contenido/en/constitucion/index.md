# Constitution
- lema: The rules every app in the catalog is built by, explained one by one: what each rule says and why it exists.
- actualizado: 2026-09-29

## What the constitution is

It is the set of rules behind **all** of sOCratic's apps: the mobile ones, the Windows programs, the
games, and this website itself. It says which licenses can be used, how the data of the people who
use the apps is handled, what buttons and error messages must look like, how versions are numbered,
what gets checked before publishing, and much more.

It is called that because it rules: an app is not considered finished unless it follows it, and
when two rules clash, the one higher up wins.

## An experiment in AI programming

The whole catalog is an experiment in **spec-driven development**: before any code is written, we
write down what each app must do (its specification) and the rules it follows, and **large language
models** (LLMs), a kind of artificial intelligence, write the code from that. The idea is to learn
what can be done this way and how to do it well.

The constitution is **the fixed part of those specifications**: the part that applies to every app.
Each app adds its own (what it does, which screens it has), but they all start from these rules: how
the code has to turn out, what must never be done, and what has to be checked before anything is
accepted. The one who publishes each version, and answers for it, is a person.

## Why it exists

Almost no rule was born on a whiteboard. Most were written **after a real mistake**: an app
rejected by a store, a version that could not be installed, hours of work lost, text the user typed
that disappeared. Every time something like that happens, the rule that would have prevented it is
written down, often with the case in parentheses. The constitution is not a list of good
intentions: it is what it cost to find out.

## It is public and applies to the whole catalog

The full text is on GitHub, under the same MIT license as the code, and every app includes it inside
its own repository. It is edited in one place and reaches all of them: that way none is left with an
old copy.

Here it is explained for anyone who wants to learn how careful software is made. Each page
summarizes one document rule by rule, in plain language, with **what it says** and **why**. What is
purely internal (working paths, where keys are stored, account and server identifiers) is not
reproduced: the idea is explained instead. And, as on the rest of the website, products that are
not from Microsoft or Google are described by what they are instead of being named.

## How it is organized

The **general constitution** is the top layer and applies to everything. Each category (mobile,
Windows tools, games, and web) has its own document, which **extends** the general one but never
contradicts it. Below them are the **technical annexes**, with the exhaustive detail for each
platform. If a document ever contradicts the general one, the general one rules and the other is
corrected.

## How it is kept up to date

When something new is learned, the rule is written into the constitution with its reason and
carried over to every app. And when the constitution changes, **its page on this website changes in
the same cycle**, in Spanish and in English. Each page states the date of the text it explains.

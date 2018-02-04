#!/bin/bash
#
# Print Playerctl metadata - for Polybar
# Rafael Cavalcanti

artist="$(playerctl metadata xesam:artist)"
title="$(playerctl metadata xesam:title)"
stat="$(playerctl status)"

case "$stat" in
	Paused)
		symb=""
		;;
	Playing)
		symb=""
		;;
esac

if [[ "$artist" == "" || "$title" == "" ]]
then
	printf "%s No info" "$symb"
else
	printf "%s %s - %s\n" "$symb" "$artist" "$title"
fi
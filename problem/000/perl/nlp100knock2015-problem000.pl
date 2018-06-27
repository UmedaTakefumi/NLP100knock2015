#!/usr/bin/env perl

use strict;
use warnings;

use Data::Dumper;

my $char = "stressed";
my @char = split(//,$char);

#print Dumper @char;

print reverse(@char) . "\n";

# Quark
[![Build Status](https://travis-ci.org/datawire/quark.svg?branch=master)](https://travis-ci.org/datawire/quark)
[![Slack](https://datawire-quark.herokuapp.com/badge.svg?dummy)](https://datawire-quark.herokuapp.com)

Quark is a specialized language for defining and implementing
communication protocols in multiple languages. In particular,
protocols that have semantics that require sophisticated client
behavior are well suited to Quark.

# Motivation

As distributed systems have proliferated (e.g., microservices), the
need for more sophisticated protocols that incorporate backpressure,
failover, retries, timeouts, rate limiting, and other behavior has
increased. Unfortunately, this sophistication introduces more
complexity in implementation. In turn, implementation complexity
reduces adoption because supporting a protocol implementation in
multiple languages requires manual porting.

Quark addresses this problem by enabling protocol authors to write a
single canonical implementation in the Quark language. The Quark
compiler then generates idiomatic implementations of the protocol in
multiple languages (currently Java, JavaScript, and Python, with Ruby
support in progress).

# Use cases

The use cases for Quark are highly varied. Some examples:

* the [Slack API](https://api.slack.com/) includes rate limiting
  behavior over a WebSockets and REST API; see [slack.q](examples/slack) for an example implementation
* the [AMQP 1.0](https://www.amqp.org/resources/specifications)
  protocol requires sophisticated client behavior for flow control and
  reconnect

## Getting Started

A popular use case for Quark is to add resilience semantics for
microservice architectures. If you're interested in doing this, check
out [Datawire Connect](https://github.com/datawire/datawire-connect)
which embeds Quark.

If you're interested in using Quark directly to develop a protocol,
just install Quark:

        curl -sL https://raw.githubusercontent.com/datawire/quark/master/install.sh | sh

## Examples

Check out the examples in the [Quark Examples repository](examples):

        git clone git@github.com:datawire/quark.git
        cd quark/examples

## Running tests

If you want to easily run tests in a git checkout of Quark, you can do
so easily if you have Docker 1.11 or later installed:

        scrips/with-docker.py py.test

Or if you want to run just some of the tests:

        scripts/with-docker.py py.test -k "lib"

This will use your local checkout, so you can test changes (committed
or uncommited) that you've made locally in the current checkout.

## Next Steps

The [Quark Quick Start](http://datawire.github.io/quark/0.6/quick-start/index.html)
provides an overview of the basic installation requirements and
process, basic compile commands, and the Quark language. If you have
successfully run any of the examples linked above, you can probably
skip this book.

Please read the
[Quark Installation and Configuration Guide](http://datawire.github.io/quark/0.6/install/index.html)
for more detailed information about installation, configuration,
compilation, packaging, and documentation generation.

The [Quark Language Reference](http://datawire.github.io/quark/0.6/language-reference/index.html)
provides information about how to code in Quark and specifics about
individual language elements including keywords, operators, functions,
data types, and annotations.

The [Quark Issues list](https://github.com/datawire/quark/issues)
provides a list of known issues - please feel free to add new issues
or feature requests as you start to use Quark. You can also join
our public Slack [support channel](https://datawire-quark.herokuapp.com).

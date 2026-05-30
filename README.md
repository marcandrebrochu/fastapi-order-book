## What is this?

TL;DR: this is a trading market simulator.

This is a weekend project used to learn how to work with the FastAPI framework.

For that, I wanted something a bit more spicy than the perennial Todo demo app.
Trading markets are for some reason a fascination of mine, and I've been wanting to write a basic order book engine for a while.
For me, this as an opportunity to start with a simple model of this idea, *and* to learn about FastAPI at the same time.

By the way, for such a system I would usually start with thinkering with the model a lot more before writing the API.
I would drive the system via tests, etc etc.
In other words, I usually start a project with an "inside-out" perspective, working on the core at first.
However, my goal is to learn about an API framework specifically, so starting with an "outside-in" approach makes more sense.

## How does it work?

### In the abstract

#### Agents

An agent (a generic term meaning "one that acts or exerts power") is any participant that can trade in the market.

#### Trading pairs

Trading always happens in a trading pair, which consists of a two assets:
the base asset, which is what is being bought or sold, and the quote asset, which is what the base asset is priced in.
Each asset is identified by a symbol (also called a "ticker").
A trading pair is written as `BASE SYMBOL/QUOTE SYMBOL`.

For instance, an agent could be interested in exchanging chickpeas (symbol: `CHKP`) for cactus seeds (symbol: `CACTUS`).
They can do so via the `CHKP/CACTUS` pair, where chickpeas are quoted in cactus seeds.
The inverse pair `CACTUS/CHKP` also exists conceptually, but as market operators we avoid listing both a pair and its dual simultaneously.

#### Orders

Within a trading pair, agents interact by placing orders to buy or sell the base asset in exchange for the quote asset.
To place an order, an agent must specify:

- the side, either buy or sell;
- the quantity of the base asset that it wants to buy or sell;
- the type, either a market order or a limit order.

In case the order is a limit order, the agent must also specify a price.
This determines the amount of quote asset per unit of base asset they're willing to trade at.
On the other hand, market orders are executed immediately against the best available counterparty price.
A market buy executes against the lowest available ask.
A market sell executes against the highest available bid.

#### Order book & matching

Active limit orders for a pair accumulate in the order book for that pair.
At any point, the order book exposes two key prices, the bid and the ask.
The bid is the highest price any buyer is currently willing to accept.
The ask is the lowest price any seller is currently willing to accept.

A buy and a sell order are matched and a trade occurs when the buying price is at least the selling price.
Market orders match unconditionally at the best available price.

When the quantities of two matched orders differ, only one is fully filled; the other is partially filled and remains active.

#### Example scenario

Agent A places a limit buy order for 10 `CHKP` at 1 `CACTUS` each, making A the highest bidder.
Later, agent B places a market sell order for 6 `CHKP`.
Since A holds the best bid, B's order matches against A's.
The trade settles 6 `CHKP`: B's order is fully filled, while A's is partially filled, leaving an active limit buy for 4 `CHKP` at 1 `CACTUS`.

### Realized as an API

TODO
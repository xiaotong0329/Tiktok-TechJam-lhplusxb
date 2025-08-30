// Copyright 2024 The Lynx Authors. All rights reserved.
// Licensed under the Apache License Version 2.0 that can be found in the
// LICENSE file in the root directory of this source tree.
import '@testing-library/jest-dom';
import { getQueriesForElement, render } from '@lynx-js/react/testing-library';
import { expect, test } from 'vitest';

import { App } from '../App.jsx';

test('App', async () => {
  render(<App />);

  const { findByText } = getQueriesForElement(elementTree.root!);

  const element = await findByText('Mood Journal');
  expect(element).toBeInTheDocument();
  expect(element).toMatchInlineSnapshot(`
    <text
      class="auth-title"
    >
      Mood Journal
    </text>
  `);
});

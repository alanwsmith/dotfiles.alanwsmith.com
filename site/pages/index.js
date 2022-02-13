import HeadTag from '../components/HeadTag'
import CodeBlock from '../components/CodeBlock'

export default function HomePage() {
  const exampleCode = `
const some_var = 'a value'
const some_object = { key: 'value' }
`

  return (
    <>
      <HeadTag
        description="Next.js Starter from Alan W. Smith"
        image="https://nextjs-starter.alanwsmith.com/og-images/main.png"
        title="Next.js Starter from Alan W. Smith"
        type="website"
        url="https://nextjs-starter.alanwsmith.com/"
      />
      <h1>Next.js Starter</h1>
      <ul>
        <li>This is a basic Next.js starter with Tailwind installed. </li>
        <li>
          It contains a basic setup for favicons and Open Graph (OG) images.{' '}
        </li>
        <li>
          The source code for the site is contained in a `site` subdirectory off
          the project root.
        </li>{' '}
        <li>
          A `netlify.toml` file and the `@netlify/plugin-nextjs` module are
          installed for deployment on Netlify.
        </li>
        <li>
          Code syntax highlighting via prism is also included. For example
          <br />
          <CodeBlock code={exampleCode} language="jsx" />
        </li>
      </ul>
      <p>More details are in the README file</p>
    </>
  )
}

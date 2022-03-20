import HeadTag from '../components/HeadTag'

export default function HomePage() {
  return (
    <>
      <HeadTag
        description="The personal dotfiles of Alan W. Smith"
        image="https://dotfiles.alanwsmith.com/og-images/main.png"
        title="The Dotfiles Of Alan"
        type="website"
        url="https://dotfiles.alanwsmith.com/"
      />
      <h1>dotfiles.alanwsmith.com</h1>
      <ul>
        <li>This is where I'll be hosting all my &quot;dotfiles&quot;</li>
      </ul>
    </>
  )
}
